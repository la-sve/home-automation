#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

# Standard-Laufzeit für Motor #34
DEFAULTDELAY = 30

class Rollo:
    """ Zustand und Steuerung eines einzelnen Rollos. """
    def __init__(self, num = 0):
        self.num = num   # Nummer des Fensters
        self.timer = 0 # Wie lange ist das Rollo schon aktiv
        self.active = False  # Ist das Rollo gerade an?
        self.dir = 0 # Welche Richtung? (Binärcodiert auf den letzten zwei bit)
        self.lastchange = 0 # Entprellen
        self.delay = DEFAULTDELAY # Standard-Laufzeit

    def update(self, up = False, down = False):
        """ Statusvariablen aktualisieren. Entweder nach Auftreten eines Interrupts oder nach
            festem Zeitintervall. 
            Rückgabe entspricht dem neuen Ansteuerwert für die zwei Pins Hoch / Runter
        """
        dir_new = (1 if up else 0) + (2 if down else 0)
        
        # Anhalten, wenn beide Taster gleichzeitig gedrückt sind.
        if up and down:
            print('stopping because up and down is pressed')
            return self.stop()
        
        if self.active:  # Eine Ausgabe ist bereits aktiv

            # Richtungsänderung bei aktiver Motoransteuerung führt zum Stoppen
            if (self.dir != dir_new) & (dir_new != 0):
                self.lastchange = time.time()
                print('stopping because of direction change while motor active')
                return self.stop()

            # Wenn Update aufgrund eines Timer-Interrupts aufgerufen wurde, 
            # Zeit weiterlaufen lassen und nichts tun

        else:   # Noch keine Ausgabe aktiv
            # Nur weitermachen, wenn überhaupt ein Button gedrückt ist.
            if (dir_new == 0):
                return self.stop()

            # Nur weitermachen, wenn Entprellzeit (500ms) abgelaufen ist TODO: Was ist bei ueberlauf nach 50 Tagen?
            #     if ((millis() - this->lastChange) < 500) return this->stop();
            if (time.time() - self.lastchange) < 0.5:
                print('rollo activation requestet, but last button press was too frequent')
                return self.stop()

            self.timer = time.time()
            self.dir = dir_new
            
        # Wenn Zeit abgelaufen ist
        if (time.time() - self.timer) > self.delay:  
            print('rollo for window %i stops because time is over' % (self.num))
            return self.stop()

        # Restliche Variablen setzen
        self.active = True
        return self.dir

    def stop(self):
        self.active = False
        self.timer = 0
        self.delay = DEFAULTDELAY  # Laufzeit wieder auf Standard zurücksetzen
        return 0

if __name__ == "__main__":
    r = Rollo()
    print("%f" % (r.update(up = False, down = False)))
    time.sleep(1)
    print("%f" % (r.update(up = True, down = False)))
    for i in range(7):
        time.sleep(1)
        print("%f" % (r.update(up = False, down = False)))