#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import smbus
import threading
import time
from rolloctl.module import RolloModule

import RPi.GPIO as GPIO
import sys
        

lock_i2c = threading.Lock()

class RolloAutomationManager(threading.Thread):
    """ Veraltet die verschiedenen Rollo Module und kommuniziert mit Home Assistant. """
    def __init__(self, module_config, bus = 1, interrupt_gpio = None):
        threading.Thread.__init__(self)
        self.running = True
        self.time = time.time()

        # I2C Bus verwenden (1 ist Standard auf Raspi 2 und 3)
        bus = smbus.SMBus(bus)
        # An welchen Raspi-Pin ist die Interrupt-Leitung der Rollo-Module angeschlossen?
        self._interrupt_gpio = interrupt_gpio

        # i2c funktionalitäten Verriegeln
        lock_i2c.acquire()

        # Rollo-Module initialisieren
        self.modules = []
        self.windows = {}
        for module in module_config:
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
            state_interruptpin = GPIO.input(self._interrupt_gpio)
            if state_interruptpin == False:
                print('Raspi interrupt pin is still low after update. Execute additional update.')
                self.update(self._interrupt_gpio)
            
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

