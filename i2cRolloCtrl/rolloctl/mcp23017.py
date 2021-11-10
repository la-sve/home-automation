# -*- coding: utf-8 -*-

# Code and comments are based on different sources. I will state them here for later
# evaluation regarding license information.
#
# https://github.com/sensorberg/MCP23017-python
# https://www.abelectronics.co.uk/kb/article/1094/i2c-part-4---programming-i-c-with-python
# https://stackoverflow.com/questions/41266273/getting-the-info-from-mcp23017-with-python
# https://roboticsbackend.com/raspberry-pi-gpio-interrupts-tutorial/

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

# Adresse kann bspw. auf Kommandozeile per "i2cdetect 1" herausgefunden werden. 1 steht für I2C Bus Nummer.

IODIRA   = 0x00  # IO direction A - 1= input 0 = output
IODIRB   = 0x01  # IO direction B - 1= input 0 = output
IPOLA    = 0x02  # Input polarity A
IPOLB    = 0x03  # Input polarity B
GPINTENA = 0x04  # Interrupt-onchange A
GPINTENB = 0x05  # Interrupt-onchange B
DEFVALA  = 0x06  # Default value for port A
DEFVALB  = 0x07  # Default value for port B
INTCONA  = 0x08  # Interrupt control register for port A
INTCONB  = 0x09  # Interrupt control register for port B
IOCONA   = 0x0A  # Configuration register
IOCONB   = 0x0B  # TODO: Macht A und B hier Sinn?
GPPUA    = 0x0C  # Pull-up resistors for port A
GPPUB    = 0x0D  # Pull-up resistors for port B
INTFA    = 0x0E  # Interrupt condition for port A
INTFB    = 0x0F  # Interrupt condition for port B
INTCAPA  = 0x10  # Interrupt capture for port A
INTCAPB  = 0x11  # Interrupt capture for port B
GPIOA    = 0x12  # Data port A
GPIOB    = 0x13  # Data port B
OLATA    = 0x14  # Output latches A
OLATB    = 0x15  # Output latches B
ALL_OFFSET = [IODIRA, IODIRB, IPOLA, IPOLB, GPINTENA, GPINTENB, DEFVALA, DEFVALB, INTCONA, INTCONB, IOCONA, IOCONB, GPPUA, GPPUB, GPIOA, GPIOB, OLATA, OLATB]

# Bits for Configuration register IOCON
BANK_BIT    = 7 # Controls how the registers are addressed
                # 1 = The registers associated with each port are separated into different banks.
                # 0 = The registers are in the same bank (addresses are sequential
MIRROR_BIT  = 6 # INT Pins Mirror bit
                # 1 = The INT pins are internally connected
                # 0 = The INT pins are not connected. INTA is associated with PORTA and INTB is associated with PORTB
SEQOP_BIT   = 5 # Sequential Operation mode bit
                # 1 = Sequential operation disabled; address pointer does not increment.
                # 0 = Sequential operation enabled; address pointer increments
DISSLW_BIT  = 4 # Slew Rate control bit for SDA output
                # 1 = Slew rate disabled
                # 0 = Slew rate enable
HAEN_BIT    = 3 # Hardware Address Enable bit (MCP23S17 only)
                # 1 = Enables the MCP23S17 address pins.
                # 0 = Disables the MCP23S17 address pins
ODR_BIT     = 2 # Configures the INT pin as an open-drain output
                # 1 = Open-drain output (overrides the INTPOL bit.)
                # 0 = Active driver output (INTPOL bit sets the polarity.
INTPOL_BIT  = 1 # This bit sets the polarity of the INT output pin
                # 1 = Active-high
                # 0 = Active-low

GPA0 = 0
GPA1 = 1
GPA2 = 2
GPA3 = 3
GPA4 = 4
GPA5 = 5
GPA6 = 6
GPA7 = 7
GPB0 = 8
GPB1 = 9
GPB2 = 10
GPB3 = 11
GPB4 = 12
GPB5 = 13
GPB6 = 14
GPB7 = 15
ALL_GPIO = [GPA0, GPA1, GPA2, GPA3, GPA4, GPA5, GPA6, GPA7, GPB0, GPB1, GPB2, GPB3, GPB4, GPB5, GPB6, GPB7]

HIGH = 0xFF
LOW = 0x00

INPUT = 0xFF
OUTPUT = 0x00


class MCP23017:
    """
    MCP23017 class to handle ICs register setup

    RegName  |ADR | bit7    | bit6   | bit5   | bit4   | bit3   | bit2   | bit1   | bit0   | POR/RST
    --------------------------------------------------------------------------------------------------
    IODIRA   | 00 | IO7     | IO6    | IO5    | IO4    | IO3    | IO2    | IO1    | IO0    | 1111 1111
    IODIRB   | 01 | IO7     | IO6    | IO5    | IO4    | IO3    | IO2    | IO1    | IO0    | 1111 1111
    IPOLA    | 02 | IP7     | IP6    | IP5    | IP4    | IP3    | IP2    | IP1    | IP0    | 0000 0000
    IPOLB    | 03 | IP7     | IP6    | IP5    | IP4    | IP3    | IP2    | IP1    | IP0    | 0000 0000
    GPINTENA | 04 | GPINT7  | GPINT6 | GPINT5 | GPINT4 | GPINT3 | GPINT2 | GPINT1 | GPINT0 | 0000 0000
    GPINTENB | 05 | GPINT7  | GPINT6 | GPINT5 | GPINT4 | GPINT3 | GPINT2 | GPINT1 | GPINT0 | 0000 0000
    DEFVALA  | 06 | DEF7    | DEF6   | DEF5   | DEF4   | DEF3   | DEF2   | DEF1   | DEF0   | 0000 0000
    DEFVALB  | 07 | DEF7    | DEF6   | DEF5   | DEF4   | DEF3   | DEF2   | DEF1   | DEF0   | 0000 0000
    INTCONA  | 08 | IOC7    | IOC6   | IOC5   | IOC4   | IOC3   | IOC2   | IOC1   | IOC0   | 0000 0000
    INTCONB  | 09 | IOC7    | IOC6   | IOC5   | IOC4   | IOC3   | IOC2   | IOC1   | IOC0   | 0000 0000
    IOCON    | 0A | BANK    | MIRROR | SEQOP  | DISSLW | HAEN   | ODR    | INTPOL | -      | 0000 0000
    IOCON    | 0B | BANK    | MIRROR | SEQOP  | DISSLW | HAEN   | ODR    | INTPOL | -      | 0000 0000
    GPPUA    | 0C | PU7     | PU6    | PU5    | PU4    | PU3    | PU2    | PU1    | PU0    | 0000 0000
    GPPUB    | 0D | PU7     | PU6    | PU5    | PU4    | PU3    | PU2    | PU1    | PU0    | 0000 0000


    """

    def __init__(self, bus, address):
        self.address = address
        self.bus = bus
        # self.address_map = {
        # 0x00: 'IODIRA',   0x01: 'IODIRB',   0x02: 'IPOLA',   0x03: 'IPOLB',
        # 0x04: 'GPINTENA', 0x05: 'GPINTENB', 0x06: 'DEFVALA', 0x07: 'DEVFALB',
        # 0x08: 'INTCONA',  0x09: 'INTCONB',  0x0a: 'IOCON',   0x0b: 'IOCON',
        # 0x0c: 'GPPUA',    0x0d: 'GPPUB',    0x0e: 'INTFA',   0x0f: 'INTFB',
        # 0x10: 'INTCAPA',  0x11: 'INTCAPB',  0x12: 'GPIOA',   0x13: 'GPIOB',
        # 0x14: 'OLATA',    0x15: 'OLATB'
        # }
        # self.register_map = {value: key for key, value in self.address_map.iteritems()}
        # self.max_len = max(len(key) for key in self.register_map)
        
    def getIoDir(self):
        return [self.bus.read_byte_data(self.address, IODIRA),
                self.bus.read_byte_data(self.address, IODIRB)]

    def getIOCON(self):
        return [self.bus.read_byte_data(self.address, IOCONA),
                self.bus.read_byte_data(self.address, IOCONB)]

    def getGPINTEN(self):
        return [self.bus.read_byte_data(self.address, GPINTENA),
                self.bus.read_byte_data(self.address, GPINTENB)]

    def getINTCAP(self):
        return [self.bus.read_byte_data(self.address, INTCAPA),
                self.bus.read_byte_data(self.address, INTCAPB)]

    def getINTF(self):
        return [self.bus.read_byte_data(self.address, INTFA),
                self.bus.read_byte_data(self.address, INTFB)]

    def getGPIO(self):
        return [self.bus.read_byte_data(self.address, GPIOA),
                self.bus.read_byte_data(self.address, GPIOB)]

    def getGPIOA(self):
        return self.bus.read_byte_data(self.address, GPIOA)

    def getGPIOB(self):
        return self.bus.read_byte_data(self.address, GPIOB)

    def setGPIOB(self,v):
        self.bus.write_byte_data(self.address, GPIOB, v)

    def pin_mode(self, gpio, mode):
        """
        Sets the given GPIO to the given mode INPUT or OUTPUT
        :param gpio: the GPIO to set the mode to
        :param mode: one of INPUT or OUTPUT
        """
        pair = self.get_offset_gpio_tuple([IODIRA, IODIRB], gpio)
        self.set_bit_enabled(pair[0], pair[1], True if mode is INPUT else False)

    def digital_write(self, gpio, direction):
        """
        Sets the given GPIO to the given direction HIGH or LOW
        :param gpio: the GPIO to set the direction to
        :param direction: one of HIGH or LOW
        """
        pair = self.get_offset_gpio_tuple([OLATA, OLATB], gpio)
        self.set_bit_enabled(pair[0], pair[1], True if direction is HIGH else False)

    def digital_read_all(self):
        """
        Reads the current direction of the given GPIO
        :param gpio: the GPIO to read from
        :return:
        """
        return [self.bus.read_byte_data(self.address, GPIOA),
                self.bus.read_byte_data(self.address, GPIOB)]

    def set_interrupt(self, gpio, enabled):
        """
        Enables or disables the interrupt of a given GPIO
        :param gpio: the GPIO where the interrupt needs to be set, this needs to be one of GPAn or GPBn constants
        :param enabled: enable or disable the interrupt
        """
        pair = self.get_offset_gpio_tuple([GPINTENA, GPINTENB], gpio)
        self.set_bit_enabled(pair[0], pair[1], enabled)

    def set_interrupt_mirror(self, enable):
        """
        Enables or disables the interrupt mirroring
        :param enable: enable or disable the interrupt mirroring
        """
        self.set_bit_enabled(IOCONA, MIRROR_BIT, enable)
        self.set_bit_enabled(IOCONB, MIRROR_BIT, enable)

    def set_interrupt_opendrain(self, enable):
        """
        """
        self.set_bit_enabled(IOCONA, ODR_BIT, enable)
        self.set_bit_enabled(IOCONB, ODR_BIT, enable)

    def set_interrupt_polarity(self, polarity):
        """
        """
        enable = (1 if polarity else 0)
        self.set_bit_enabled(IOCONA, INTPOL_BIT, enable)
        self.set_bit_enabled(IOCONB, INTPOL_BIT, enable)

    def read(self, offset):
        return self.bus.read_byte_data(self.address, offset)

    def write(self, offset, value):
        return self.bus.write_byte_data(self.address, offset, value)

    def get_offset_gpio_tuple(self, offsets, gpio):
        if offsets[0] not in ALL_OFFSET or offsets[1] not in ALL_OFFSET:
            raise TypeError("offsets must contain a valid offset address. See description for help")
        if gpio not in ALL_GPIO:
            raise TypeError("pin must be one of GPAn or GPBn. See description for help")

        offset = offsets[0] if gpio < 8 else offsets[1]
        _gpio = gpio % 8
        return (offset, _gpio)

    def set_bit_enabled(self, offset, gpio, enable):
        stateBefore = self.bus.read_byte_data(self.address, offset)
        value = (stateBefore | self.bitmask(gpio)) if enable else (stateBefore & ~self.bitmask(gpio))
        self.bus.write_byte_data(self.address, offset, value)

    def bitmask(self, gpio):
        return 1 << (gpio % 8)
