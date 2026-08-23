# Lüftungssteuerung Dokumentation

Dokumentation zur Lüftungssteuerung.
Diese neue und hier beschriebene ESPHome basierte Steuerung ersetzt die Steuerplatine einer zentralen kontrollierten Wohnraumlüftung (KWL). 
Es handelt sich um das Gerät Kermi x-well N300 mit Bedieneinheit CR300 aus dem Jahr 2015. In der Standard-Ausführung. Keine zusätzlichen optionalen Komponenten (wie CO2 Sensor oder ähnliches) sind in der Anlage verbaut.

## Hardwarekomponenten

### 1x Mikrocontroller Board
(Ersetzt die Hauptplatine der KWL.)

Typ: Waveshare ESP32-S3-ETH-Development-Board

### 3x Relais
(Neu)

Typ: finder 34.51.7.024.0010
(24 V DC) 
Sockel 93.01.7.024 

R1: Bypass Klappe Anschluss 3
R2: Bypass Klappe Anschluss 2
R3: Ventilator Zuluft und Abluft

R1 und R2 sind hardwareseitig gegeneinander verriegelt. D.h. COM von R2 ist an 220V AC angeschlossen. NC von R2 ist an COM von R1 angeschlossen. NO von R1 an Bypass und NO von R2 an Bypass.

### 1x Netzteil (24V DC 15W)
(Ersetzt das Originalnetzteil.)

Typ: Meanwell HDR-15-24

### 1x DCDC Wandler für Mikrocontroller Board
(Neu)

Typ: 24V DC -> 5V DC 3A USB Buchse

### DFRobot GP8403 Breakout-Board mit I2C
(Neu)

Für Ansteuerung Ventilatoren 0-10V
- VOUT0: Abluft Ventilator
- VOUT1: Zuluft Ventilator  

### 1x 4-Kanal Optokoppler Modul (3,3V auf 24V)
(Neu)

Zum Schalten der Relais

### 2x Lüfter: ebmpapst, R3G190-RG19-33
(Original-Komponenten des Gerätes.)

Steckerbelegung:
- Kabel 1:
  - Blau: GND
  - Gelb: 0-10V Steuersignal
  - Rot: 10V Output
  - Weiß: Tacho-Signal 
- Kabel 2:
  - N 
  - L
  - PE 

### 1x Bypass: Klappenantrieb BELIMO CM230-F-L 2Nm 100...240VAC
(Original-Komponente des Gerätes.)

### 4x OneWire Temperatursensor DS18B20
(Ersetzen die NTC Fühler des Originalgerätes.)

- T1: Außenluft
- T2: Zuluft nach Wärmetauscher
- T3: Abluft / Raumtemperatur
- T4: Abluft nach Wärmetauscher

### 1x GY-21-HTU21D Breakout-Board mit I2C
(Ersetzt den Feuchtigkeits Sensor des Originalgerätes.)

## Verbindungen

### Mikrocontroller Board

- GPIO 39: Optokoppler Modul IN1 -> Relais 1, Bypass 1
- GPIO 40: Optokoppler Modul IN2 -> Relais 2, Bypass 2
- GPIO 41: Optokoppler Modul IN3 -> Relais 3, Ventilatoren
- GPIO 42: Optokoppler Modul IN4 -> Nicht belegt

- GPIO 47: Tacho Zuluft
- GPIO 48: Tacho Abluft

- GPIO 33: 0-10V Steuersignal 1
- GPIO 34: 0-10V Steuersignal 2

- GPIO 35: T1 OneWire
- GPIO 36: T2 OneWire
- GPIO 37: T3 OneWire
- GPIO 38: T4 OneWire

- GPIO 33: I2C SCL (GP8403 Modul)
- GPIO 34: I2C SDA (GP8403 Modul)

- GPIO 16: I2C SCL (GY-21-HTU21D Modul)
- GPIO 18: I2C SDA (GY-21-HTU21D Modul)


## Funktionalität
Die Steuerung soll folgende Funktionsmodi unterstützen:
- Aus
- Wartungsmodus
- Automatik Modus

### Wartungsmodus
Der Nutzer kann sämtliche Aktoren direkt über Home Assistant ansteuern.

### Automatik Modus
TODO

### Aus
Grundzustand des Gerätes. Relais für Lüfter aus. BypassKlappe geschlossen.