#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mcp23017
import Rollo

class RolloModule(mcp23017.MCP23017):
    def __init__(self, bus, address, unusedPins=0):
        super().__init__(bus, address)
        
        # Einstellen der Interrupt-Pins für Port A und Port B
        # Wir schalten mirroring aus und ...
        # Da wir mehrere MCPs an einem Interrupt Pin des Arduino betreiben möchten, müssen 
        # wir mit open drain arbeiten. D.h. wir arbeiten mit einem 10k pull up am Arduino-Pin und
        # verbinden die Interrupt-Ausgänge der MCPs alle miteinander. Durch open drain zieht ein
        # beliebiger Interrupt die Leitung auf Masse. (Mirroring bleibt aus)
        self.set_interrupt_mirror(False)
        self.set_interrupt_opendrain(True)
        self.set_interrupt_polarity(mcp23017.LOW)

        # Port A am MCP muss als Input konfiguriert werden, hier kommen unsere 24V Button-Signale
        # (auf 5V reduziert durch Spannungsteiler) an. Ein Interrupt soll ausgelöst werden, sobald
        # sich der Status des Buttons ändert.
        for pin in range(8 - unusedPins):
            self.pin_mode(pin, mcp23017.INPUT)
            self.set_interrupt(pin, True) #CHANGE

        # Unverbundene Eingangs-Pins (Port A) sind durch Spannungsteiler mit GND verbunden. 
        # Wir konfigurieren sie als input und aktivieren keinen Interrupt.
        for pin in range(8-unusedPins,8):
            self.pin_mode(pin, mcp23017.INPUT)
            self.set_interrupt(pin, False)

        # Port B wird als Output definiert. Hier hängt unser Darlington-Array dran
        for pin in range(8,16):
            self.pin_mode(pin, mcp23017.OUTPUT)

        # Alle Outputs zunächst zurücksetzen
        self.setGPIOB(0)

        # Wir speichern den aktuellen Zustand
        self.outputstate = self.getGPIOB
        
        # Speichern der Rollo-Instanzen
        self.rollos = []

    def addWindow(self,num):
        print(f"Adding window {num} to rollo module with address: 0x{self.address:02x}")
        self.rollos.append(Rollo.Rollo(num))

    def state(self, pin):
        """ Zurückgeben des Zustands vom gesuchten Pin 1...8 """
        if pin > 8: pin = 8
        if pin < 1: pin = 1
        self.updateOutputOnly()
        return (True if (self.outputstate & (1 << (pin-1))) else False)

    def activate(self, rollo_index, cmd):
        if rollo_index < len(self.rollos):
            if cmd == 'stop': 
                self.rollos[rollo_index].stop()
            elif cmd == 'open': 
                self.rollos[rollo_index].update(True, False)
            elif cmd == 'close': 
                self.rollos[rollo_index].update(False, True)
            else:
                print('Command %s not valid!' % (cmd))
        else:
            return False

    def update(self):
        """ Alle Rollo Instanzen durchgehen und entsprechend Ausgabeports setzen. """

        # Ein- und Ausgangsstatus auslesen (gleichzeitg wird Interrupt-Flag geleert)
        intflag_a, intflag_b         = self.getINTF()      # Which port triggert the interrupt? (also clears the interrupt flags)
        intstate_a, intstate_b       = self.getINTCAP()    # Port Values at the time, the interrupt occured
        inputstate, self.outputstate = self.getGPIO()      # Current State

        # Wir wollen nur reagieren, wenn Input Pin von LOW auf HIGH wechselte.
        if (intflag_a & intstate_a) > 0:
            print("MCP23017 ADRESS: " + f"{self.address:#02x}")
            print("INPUT PORT           |  OUTPUT PORT       ")
            print("---------------------|--------------------")
            print("INTFA    : " + f"{intflag_a:08b}"     + "  |  INTFB    :" + f"{intflag_b:08b}"           + "  -> Which port triggert the interrupt?") # f-String Format
            print("INTCAPA  : " + f"{intstate_a:08b}"    + "  |  INTCAPB  :" + f"{intstate_b:08b}"          + "  -> States at the moment, the interrupt occured.") # f-String Format
            print("GPIOA    : " + f"{inputstate:08b}"    + "  |  GPIOB    :" + f"{self.outputstate:08b}"    + "  -> Current State") # f-String Format
        
        self.updateOutputOnly(intstate_a)


    def updateOutputOnly(self, inputstate = 0):
        """ 
        Die Rollo-Instanzen werden nach ihrem aktuellen Wunsch-Zustand abgefragt.
        Sollte ein Input-State gegeben sein, bspw. weil ein Taster gedrückt wurde, wird dieser berücksichtigt.
        Entspricht der gemeinsame Wunschzustand aller angeschlossenen Rollos nicht dem aktuellen Ausgangsport,
        wird der Ausgangsport entsprechend neu gesetzt.
        """
        new_state_b = self.calcOutputState(inputstate)
        if new_state_b != self.outputstate:
            self.setGPIOB(new_state_b)
            self.outputstate = new_state_b

    def calcOutputState(self, inputstate):
        """
        Zustände der Rollos anhand des Eingangsstatus Byte aktualisieren und
        Zustände der Rollos in ein neues Ausgangs-Byte wandeln
        """
        #TEST: print(f"{(2 | 2 << 2 | 0 << 4 | 3 << 6):08b}")
        new_state_b = 0
        for i,rollo in enumerate(self.rollos): 
            up = inputstate & (1 << (i*2))
            down = inputstate & (1 << (i*2+1))
            new_state_b |= rollo.update(up, down) << (i*2)
        return new_state_b

    def printProperties(self):
        print("INPUT PORT           |  OUTPUT PORT       ")
        print("---------------------|--------------------")
        ret = self.getIoDir()
        print("IODIRA   : " + f"{ret[0]:08b}" + "  |  IODIRB   :" + f"{ret[1]:08b}") # f-String Format
        ret = self.getGPINTEN()
        print("GPINTENA : " + f"{ret[0]:08b}" + "  |  GPINTENB :" + f"{ret[1]:08b}") # f-String Format
        ret = self.getIOCON()
        print("IOCONA   : " + f"{ret[0]:08b}" + "  |  IOCONB   :" + f"{ret[1]:08b}") # f-String Format
        ret = self.getINTCAP()
        print("INTCAPA  : " + f"{ret[0]:08b}" + "  |  INTCAPB  :" + f"{ret[1]:08b}") # f-String Format
