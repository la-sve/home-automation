#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smbus
import threading
import time
from RolloModule import RolloModule

import RPi.GPIO as GPIO
import signal
import sys

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

        # Adresse kann bspw. auf Kommandozeile per "i2cdetect 1" herausgefunden werden. 1 steht für I2C Bus Nummer.
        address = 0x21

        # I2C Bus verwenden (1 ist Standard auf Raspi 2 und 3)
        bus = smbus.SMBus(1)

        # Rollo-Module initialisieren
        lock_i2c.acquire()
        self.m1 = RolloModule(bus, address, unusedPins=4)
        self.m1.addWindow(1)
        self.m1.addWindow(2)

        self.m1.printProperties()
        lock_i2c.release()

        # Sind wir momentan in der update methode?
        self.updating = False

    def run(self):
        """ 
        Regelmäßig Zustände überprüfen.
        Aktualisiert die Rollo-Modul-Ausgänge, falls Zeiten für die Rollo-Bewegung abgelaufen sind.
        """
        while self.running:
            #self.m1.manualUp(1)   #TEST

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
            self.m1.update()
        else:
            self.m1.updateOutputOnly()

        # i2c für andere threads wieder freigeben
        self.updating = False
        lock_i2c.release()        



if __name__ == "__main__":
    manager = RolloAutomationManager()

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(RASPIINTPIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(RASPIINTPIN, GPIO.FALLING, 
            callback=manager.newInputDetected)  #, bouncetime=10

    try:
        manager.start()
        while True:
            time.sleep(10)
            print('MainLoop')
    except (KeyboardInterrupt, SystemExit):
        manager.running = False
        manager.join()
        GPIO.cleanup()
        sys.exit(0)

    # signal.signal(signal.SIGINT, signal_handler)
    # signal.pause()
