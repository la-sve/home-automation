#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import smbus
import threading
import time
from RolloModule import RolloModule

import RPi.GPIO as GPIO
import signal
import sys, os

import json

# Daten per FLASK mit Home Assistant austauschen:
# https://realpython.com/api-integration-in-python/
# https://www.home-assistant.io/integrations/switch.rest/
# https://www.home-assistant.io/integrations/rest_command/
# https://thingsmatic.com/2017/02/07/home-assistant-integrating-restful-switches/

from flask import Flask, request, jsonify
app = Flask(__name__)

# MCP23017 Adressen definieren
#  0 ... entspricht 0x20
#  1 ... entspricht 0x21
#    ...
#  A0  A1  A2  Adresse
#   0   0   0   0x20
#   1   0   0   0x21
#   0   1   0   0x22
#   1   1   0   0x23
#   0   0   1   0x24
#   1   0   1   0x25
#   0   1   1   0x26
#   1   1   1   0x27
MODULE1ADR = 0x20
MODULE2ADR = 0x21
MODULE3ADR = 0x22
MODULE4ADR = 0x23
MODULE5ADR = 0x24  # Nur 4 der 8 Input Pins werden verwendet

# Adresse kann bspw. auf Kommandozeile per "i2cdetect 1" herausgefunden werden. 1 steht für I2C Bus Nummer.
        

# Interrupt-Pin am Raspberry Pi, welcher mit Interrupt-Leitung der Rollo-Module verbunden ist.
RASPIINTPIN=17
lock_i2c = threading.Lock()

def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)


class RolloAutomationManager(threading.Thread):
    """ Veraltet die verschiedenen Rollo Module und kommuniziert mit Home Assistant. """
    def __init__(self):
        threading.Thread.__init__(self)
        self.running = True
        self.time = time.time()
        
        # Einstellungen aus json-Datei laden
        f = open(os.path.join(sys.path[0],'manager.json'))
        self.settings = json.load(f)
        f.close()

        # I2C Bus verwenden (1 ist Standard auf Raspi 2 und 3)
        bus = smbus.SMBus(1)

        # i2c funktionalitäten Verriegeln
        lock_i2c.acquire()

        # Rollo-Module initialisieren
        self.modules = []
        self.windows = {}
        for module in self.settings["modules"]:
            address = int(module["address"], base=16)
            unused = 8 - len(module["windows"])*2
            self.modules.append(RolloModule(bus, address, unusedPins=unused))
            for i, window in enumerate(module["windows"]):
                self.modules[-1].addWindow(int(window))
                self.windows[int(window)] = {
                    "module": len(self.modules)-1,
                    "rolloIndex": i}

        # Debug
        self.modules[-1].printProperties()
        self.activate(1, "open")
        
        # i2c für andere threads wieder freigeben
        lock_i2c.release()

        # Sind wir momentan in der update methode?
        self.updating = False

    def run(self):
        """ 
        Regelmäßig Zustände überprüfen.
        Aktualisiert die Rollo-Modul-Ausgänge, falls Zeiten für die Rollo-Bewegung abgelaufen sind.
        """
        while self.running:
            
            # Prüfen, ob wir uns gerade im Update-Zustand befinden. Bspw. weil dieser gerade per Interrupt
            # ausgelöst wurde.
            cnt = 0
            while self.updating:
                time.sleep(0.01)
                # Watchdog
                cnt += 1
                if cnt > 100:
                    print('Something went wrong!')
                    cnt = 0
                    #TODO: Etwas sinnvolles unternehmen!
            
            # Sicherheitshalber den Interrupt-Pin abfragen. Dieser sollte LOW sein. Wenn dies nicht
            # der Fall ist, gab es im Vorfeld einen Fehler. Zum Beheben wird ein manuelles Update
            # ausgelöst.
            state_interruptpin = GPIO.input(RASPIINTPIN)
            if state_interruptpin == False:
                print('Raspi interrupt pin is still low after update. Execute additional update.')
                self.update(RASPIINTPIN)
            
            # Rollos updaten -> relevant: Muss ein Rollo gestoppt werden, weil es bereits die entsprechende Zeit aktiv ist?
            self._updateModules()

            time.sleep(1)

            # TODO: ZUR SICHERHEIT alle 10 Sekunden MAL DEN ZUSTAND DER MCPs AUSLESEN UM INTERRUPT ZU LEEREN

    def activate(self, window, cmd, time = None):
        """ 
        Für externe Steuerung per REST Interface. 
        Änderung wird erst in der Hauptschleife (run-Methode) aktiv.
        - window 1 ... 18 
        - cmd "open" "close" "stop" 
        """

        # Modulindex für gefragtes Fenster finden
        module_index = self.windows[window]["module"]
        rollo_index = self.windows[window]["rolloIndex"]
        # Kommando an Modul weiterreichen
        self.modules[module_index].activate(rollo_index, cmd, time)
        # Änderung wird dann in der normalen Update-Schleife gesetzt

        return "true" #TODO

    def newInputDetected(self,channel):
        """ 
        Auswerten aller Rollo-Module nach einem erkannten Interrupt.
        Interrupt Signal ist an diese Methode gebunden.
        """
        self._updateModules(True)

    def _updateModules(self, force_all = False):
        """ 
        Auswerten aller Rollo-Module, d.h. alle Rollo-Modul-Instanzen durchgehen
        und deren Ausgangsports aktualisieren, falls notwendig. 
        Wenn force_all auf True, werden alle Module zunächst ausgelesen
        """
        # i2c funktionalitäten Verriegeln
        lock_i2c.acquire()
        self.updating = True
        
        if force_all == True:
            #self.m1.update()
            for module in self.modules:
                module.update()
        else:
            #self.m1.updateOutputOnly()
            for module in self.modules:
                module.updateOutputOnly()

        # i2c für andere threads wieder freigeben
        self.updating = False
        lock_i2c.release()        

# @app.route("/Shutters/<int:moduleNumber>/<int:pinNumber>", methods=["GET"])
# def get_shutters(moduleNumber, pinNumber):
#     #state = manager.state(moduleNumber,pinNumber)
#     #return ('on' if state else 'off')
#     return 50

@app.route("/Shutters",methods=["PUT","POST"])
def update_shutter_state():
    state=None
    print(request)
    if request.json is not None:
        window = int(request.json.get("window"))
        cmd = request.json.get("cmd")
        print(request.json)
        if ('time' in request.json) and request.json.get("time"):
            time = int(request.json.get("time"))
            print(f"Requested window {window} with command {cmd} and time {time}")
            state = manager.activate(window, cmd, time)
        else:
            print(f"Requested window {window} with command {cmd}")
            state = manager.activate(window, cmd)
    else:
        print("Only json formatted post requests are supported!")
        state = request.data.decode("utf-8")

    return state, 201

if __name__ == "__main__":
    manager = RolloAutomationManager()
    app.debug = False
    app.use_reloader = False

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(RASPIINTPIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(RASPIINTPIN, GPIO.FALLING, 
            callback=manager.newInputDetected)  #, bouncetime=10

    try:
        manager.start()
        threading.Thread(target=lambda: app.run(host="0.0.0.0",port=5000)).start()
        while True:
            time.sleep(10)
            print('MainLoop')
    except (KeyboardInterrupt, SystemExit):
        manager.running = False
        manager.join()
        GPIO.cleanup()
        sys.exit(0)

