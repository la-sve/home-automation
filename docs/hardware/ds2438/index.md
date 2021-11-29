# Luftfeuchtemessung
Temperatur- und Luftfeuchtemessung mit emuliertem DS2438 (Arduino Nano Clone) und HTU21D Sensor. Einbinden in Home Assistant durch Anschluss des DS2438 One-Wire Signals.

**Quellcode** im `DS2438Humidity` Verzeichnis.

## Motivation
Wenn man sich im Web umschaut, stellt man zunächst fest, dass es keinen OneWire-Sensor gibt, der die Luftfeuchtigkeit messen kann. Wird ein wenig weiter gesucht, stößt man auf kleine Selbstbau-Schaltungen, die mit Hilfe eines HIH-4030 oder HIH-5030 und einem DS2438 die Luftfeuchte messen, wie bspw. [hier](https://skyboo.net/2017/03/ds2438-based-1-wire-humidity-sensor/) oder [hier](https://www.tm3d.de/elektronik-projekte/1-wire-feuchtesensor/neuen-version-2015). Der DS2438 wird auch von der HA OneWire integration sowie dem Linux Kernel unterstützt. Ein Blick in die Home Assistant OneWire Integration verrät auch, dass der DS2438 typischerweise nicht nur für "Smart Battery Monitor" verwendet wird, sondern als "multipurpose measurement node".

## DS2438 Emulation

Beschäftigt man sich noch weiter mit der Thematik, rückt eine weitere Möglichkeit in den Vordergrund: Das Emulieren eines DS2438 und verwenden des DHT22 Sensors zur Messung von Temperatur und Luftfeuchte. Das Emulieren funktioniert bspw. mit Hilfe eines kleinen ATMEGAs und der Softwarebibliothek [OneWireHub](https://github.com/orgua/OneWireHub). Diese Variante ist etwas kostengünstiger und meiner Meinung nach Flexibler. Es ermöglicht bspw. noch weitere Sensoren mit dem ATMEGA zu verbinden, die ebenfalls nicht auf dem OneWire Protokoll basieren.

## Umsetzung

Die einfachste Variante ist meiner Meinung nach, einen Arduino Nano Clone zu verwenden und entsprechend den DHT22 damit zu verbinden. Aber achtung: Möglicherweise wird noch ein Level-Shifter benötigt, um von einem 5V Arduino auf 3,3V des Raspberry zu transformieren. 

Die OneWireHub-Bibliothek bringt bereits einige Beispiele mit, die einen [DS2438 simulieren](https://github.com/orgua/OneWireHub/blob/master/examples/DS2438_battMon/DS2438_battMon.ino) und den Arduino zum OneWire-Slave umfunktionieren. Dazu verwendete ich die Arduino GUI Version 1.8.13 und verlinkte die geclonte Bibliothek im GUI-Programmverzeichnis unter Libraries. Nun wird man schnell feststellen, dass sich die erhoffte Funktionalität nicht einstellt. Nach einiger Suche stößt man auf folgendes Issue in der OneWireHub Bibliothek: [RaspberryPi doesn't recognize OneWireHub](https://github.com/orgua/OneWireHub/issues/44). 

Die Lösung besteht im Modifizieren der Datei OneWireHub_config.h im src Verzeichnis der Bibliothek. Der Parameter `ONEWIRE_TIME_MSG_HIGH_TIMEOUT` muss wie folgt geändert werden:
`constexpr time OW_t ONEWIRE_TIME_MSG_HIGH_TIMEOUT = { 38000_us };`

Anschließend wird vom Raspberry Pi ein DS2438 auf dem OneWire Bus erkannt. 

## DHT22 Sensor
Weiter geht es mit der Einbindung des DHT22 Sensors. Dazu gibt es bereits Bibliotheken (siehe [DHT-sensor-library](https://github.com/adafruit/DHT-sensor-library)) in der Arduino-GUI (Bibliotheksverwalter), die installiert werden können:

* DHT sensor library by Adafruit
* Adafruit Unified Sensor

Das dort vorhandene Beispiel kann einfach mit dem DS2438 Beispiel kombiniert werden und liefert entsprechende Ergebnisse. 

## Umrechnung für DS2438
Zu beachten ist, dass wir die Spannungswerte des DS2438 zum Übertragen der Feuchtigkeitswerte "missbrauchen" müssen. Der Wertebereich ist entsprechend anzupassen. Da bereits einige Sensoren existieren, die den DS2438 genau dafür einsetzen, sind einige davon mit entsprechender Umrechnung bereits in OWFS implementiert. 

Um zu verstehen, wie die Werte für die unterschiedlichen Feuchtesensoren im OWFS zustande kommen, muss wohl oder übel ein Blick in den Quellcode erfolgen. 
In der entsprechenden Datei [ow_2438.c](https://github.com/owfs/owfs/blob/master/module/owlib/src/c/ow_2438.c) finden sich die Umrechungen.

Die einfachste Formel findet sich beim Typ *Humid_1735*:
> OWQ_F(owq) = 38.92 * VAD - 41.98;

(VAD ist definiert im Bereich 1.5 to 10V)

Dieser Sensor ist ebenfalls in Home Assistant implementiert, siehe [Quellcode](https://github.com/home-assistant/core/blob/dev/homeassistant/components/onewire/sensor.py). 
Entsprechend umgestellt kann nun der Feuchtewert in einen Spannungswert (einzig zum Zweck der Übertragung über den 1-WireBus) umgewandelt werden. 

*Als Anmerkung:* Einige Lösungen schlagen vor, statt des DS2438 doch lieber den DS18B20 zu simulieren, da dieser weniger komplex sei. Das Problem ergibt sich dann bei der Implementierung in Home Assistant. Diese Art der Feuchteübertragung über einen Temperatursensor ist bisher noch nicht vorgesehen...

## HTU21D Sensor

Da der DHT22 mittlerweile in die Jahre gekommen ist und das Auslesen des Sensors nur sehr langsam erfolgt, kann auch über eine Alternative nachgedacht werden. Die zweite Version des Feuchtesensors nutzt einen GY-21 Breakout Board von AZ-Delivery mit einem HTU21 Feuchtesensor. Das Breakout-Board ist bereits mit 10k Pull-Ups ausgestattet und kann direkt an den Mikrocontroller angeschlossen werden (Ebenfalls ist ein Spannungswandler verbaut, damit als VIN auch 5V verwendet werden kann).

Folgende Bibliothek kann als Startpunkt verwendet werden: [SparkFun_HTU21D_Breakout_Arduino_Library](https://github.com/sparkfun/SparkFun_HTU21D_Breakout_Arduino_Library).
Leider wartet die Bibliothek aktiv zwischen Messanforderung und Auslesen des Sensorwerts um die 50ms. Dies könnte für die OneWire Emulation problematisch werden. Entsprechend wurde die Bibliothek geringfügig modifiziert, um die aktive Wartezeit durch ein Triggern und späteres Auslesen zu ersetzen. Dazwischen können andere Programmteile ausgeführt werden.  

Der Experimentalaufbau zeigte eine Instabilität nach einigen Stunden, die sich darin äußerte, dass das Arduino-Programm "hängen" blieb. Mutmaßlich ist die I2C-Bibliothek die Ursache. Ein Ausweg bietet ein Watchdog Timer, wie es bspw. [hier](https://spellfoundry.com/2020/06/25/reliable-embedded-systems-using-the-arduino-watchdog/) beschrieben wird.

