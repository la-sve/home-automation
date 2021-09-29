#import os, sys
#file_path = 'asyncowfs/'
#sys.path.append(os.path.dirname(file_path))


import sys
import time
from pyownet import protocol

class OWDevice:
    ow = None  # Connection to owfs

    @classmethod
    def connect(cls,host,port):
        """Connect to OWFS Instance (defined as classmethod, because it is the same for all)"""
        TIMEOUT = 10
        timeout_time = time.time() + TIMEOUT
        while time.time() < timeout_time:
            try:
                cls.ow = protocol.proxy('localhost',4304, persistent=True, verbose=False)
            except protocol.ConnError:
                time.sleep(1)
            else:
                break
        else:
            # Error! creation of owp has timed out
            sys.exit('Unable to open connection to owserver')
        # Success! we have a connection to owserver
        assert cls.ow.present('/')
        print(cls.ow.dir())

class DS2408(OWDevice):
    """Repraesentiert ein Geraet"""
    devID = 29

    def __init__(self, adr):
        self.dir = "/%s.%s/" % (self.devID, adr)
        print("DS2408 Device initialized with bus path: %s" % self.dir)
        assert self.ow.present(self.dir)
        self.state = None
        self.latch = None
        self.latchActive = None  # Verglichen zum Vorgaengerschritt immernoch aktiv, um nur Flanke zu detektieren.

    def getState(self):
        """Aktuellen Status auslesen"""
        try:
            state = self.ow.read(self.dir + 'PIO.BYTE', 3, 9)
            state = state.decode("utf-8")
            state = int(state.strip())
            self.state = state
        except protocol.Error as err:
            print("Some pyownet error occured: {0}".format(err))
        return self.state

    def setState(self, state = None):
        if state is None: state = self.state
        try:
            self.ow.write(self.dir + 'PIO.BYTE', bytes("%s" % state, encoding="utf-8"))
        except protocol.Error as err:
            print("Some pyownet error occured: {0}".format(err))

    def _getLatch(self):
        """Nur privat, Latch Register ohne zuruecksetzen lesen."""
        try:
            inp = self.ow.read(self.dir + 'latch.BYTE',3,9)
            inp = inp.decode("utf-8")
            self.latch = int(inp.strip())
        except protocol.Error as err:
            print("Some pyownet error occured: {0}".format(err))
        return self.latch

    def getLatch(self):
        """Latch Register lesen und zuruecksetzen."""
        self._getLatch()
        self.resetLatch()
        return self.latch

    def getLatchRising(self):
        """Latch bits ignorieren, die im Vorgaengerschritt bereits gesetzt waren. (ersetzt Aufruf von getLatch)"""
        self.getLatch()
        # Flankendetektion
        if self.latchActive is not None:
            mNotRising = self.latchActive & self.latch
            self.latchActive = self.latch           # Neuen Wert fuer Flankendetektion speichern
            self.latch = self.latch & ~mNotRising   # Bereits detektierten Wert deaktivieren
        else:
            self.latchActive = self.latch           # Neuen Wert fuer Flankendetektion speichern
        return self.latch

    def resetLatch(self):
        """Latch Register zuruecksetzen"""
        try:
            self.ow.write(self.dir + 'latch.BYTE', bytes(b'255'))
        except protocol.Error as err:
            print("Some pyownet error occured: {0}".format(err))

    def isBitSet(value, bit_index):
        """Bitvergleich: Ist Bit im Register gesetzt?"""
        return (value >> bit_index) & 1

    def toggleBit(value, bit_index):
        """Bit umkehren
           siehe auch: https://realpython.com/python-bitwise-operators/#getting-a-bit"""
        return value ^ (1 << bit_index)

class DS2408Board:
    """Definiert ein DS2408 Board mit zwei oder einem DS2408"""
    def __init__(self, adrOut, adrIn = None):
        self.output = DS2408(adrOut)
        if adrIn is None:
            self.input = None
        else:
            self.input = DS2408(adrIn)

    def update(self):
        """Sollte in konstanten kleinen Zeitabstaenden durchgefuehrt werden. State wird als Klassenvariable gespeichert."""
        if self.input is not None:
            input = self.input.getLatchRising()
            if input:
                currentState = self.output.getState()       # Wir holen uns den aktuellen Zustand nur, wenn wir ihn brauchen. Also hier.
                print(f"State: OLD {currentState:08b} NEW {(input ^ currentState):08b}")
                self.output.setState(input ^ currentState)  # XOR

    def printState(self):
        if self.input is not None:
            print(f"IN: {self.input.latch:08b}")


def main():
    
    #proxy = protocol.proxy('localhost',4304)
    OWDevice.connect('localhost',4304)

    testboard = DS2408Board(adrOut='A00837000000',adrIn='980837000000')
    
    cnt = 0
    tStart = time.time()
    while (True):
        testboard.update()
        #testboard.printState() #debugging
        cnt += 1
        if cnt >= 100:
            tEnd = time.time()
            dt = (tEnd-tStart) / 100
            print("Execution frequency: %0.2f" % dt)
            tStart = tEnd
            cnt = 0
        time.sleep(0.05)

if __name__ == '__main__':
    main()