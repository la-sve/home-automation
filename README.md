# home-automation

As I don't believe, this project is of much relevance to others, it is described only in german. It is about my personal home automation using a lot of DS18S20 temperature sensors distributed within every room in my home for controlling my heating system via custom made DS2408 boards connected to some finder relais switching the underfloor heating on and of for individual rooms. Additionally, light switches (push buttons) are used as input to another part of the DS2408 boards to be able to use them normally besides the automation over _Home Assistant_. The later is used for automation and as user interface. Also a shutter control is realized, but with custom boards using an i2c port expander (MCP23017).

**Kurzbeschreibung:** Projektdateien zur Automatisierung eines Hauses mittels Home Assistant, RaspPi und diversen Sensoren und Aktoren auf 1-Wire Basis.

## Systemübersicht
TODO: Geräte und Verteilung per LAN

## Installation und Einrichtung

### 1-Wire Bus per GPIO auf RaspPi

-   Über `raspi-config` wird zunächst das 1-Wire Interface aktiviert.
-   Jetzt muss noch der zu verwendende Pin angegeben werden:<br>
    `> sudo vim /boot/config.txt`<br>
    > dtoverlay=w1-gpio,gpiopin=21 #DS2408 devices,  4.7kOhm external Pull-Up <br>
    > dtoverlay=w1-gpio,gpiopin=4 #DS18S20 temp devices, 1st bus 1.5kOhm external Pull-Up<br>
    > dtoverlay=w1-gpio,gpiopin=13 #DS18S20 temp devices, 2nd bus 1.5kOhm external Pull-Up<br>
    > dtoverlay=w1-gpio,gpiopin=26 #DS18S20 temp devices, 3rd bus 1.5kOhm external Pull-Up<br>
    > dtoverlay=w1-gpio,gpiopin=27 #DS18S20 temp devices, 4th bus 1.5kOhm external Pull-Up<br>
    
-   REBOOT
-   Die funktionsweise kann wie folgt geprüft werden _(Hier wurde ein DS18S20 und DS2408 angeschlossen.)_:<br>
    `> lsmod | grep -i w1_`
    ```
    w1_ds2408              16384  0
    w1_therm               28672  0
    w1_gpio                16384  0
    wire                   36864  3 w1_gpio,w1_ds2408,w1_therm
    ```
Weitere Informationen finden sich bspw. auch hier: https://pinout.xyz/pinout/1_wire#

### OWFS (1-Wire File System)
OWFS bietet ein einfaches Interface zu OneWire Geräten. Nachfolgende Software baut häufig darauf auf und weiterhin hat es den Vorteil, dass verschiedene Instanzen den Bus gleichzeitig verwenden können. Die nachfolgenden Schritte sind notwendig, um dies zu installieren. (siehe auch: https://youtu.be/rlmYxfKDni8)

`> sudo apt install owfs owserver`

Jetzt sollte bereits ein HTTP-Server laufen: http://ow.local:2121/

In der Standardkonfiguration läuft nur ein simulierter (Fake) Sensor. Wir müssen noch die vom Server zu nutzende Hardware angeben. Bspw. einen USB-OneWire-Adapter oder das Kernel-Modul zum direkten Anschluss an die GPIO Pins: <br>
` > sudo vim /etc/owfs.conf`<br>
> _Auskommentieren:_<br>
  `server: FAKE = DS18S20,DS2405`<br>
  _Einkommentieren:_<br>
  `server: w1`

Nun den OWFS Service neu starten:<br>
`> sudo systemctl restart owserver`

> _Einige Debugging Befehle:_<br>
  `> systemctl status owfs.service`<br>
  `> systemctl cat owfs.service`<br>
  `> journalctl -f`<br>

### Home Assistant
Hier kann der offiziellen Anleitung gefolgt werden. Dabei wird die Variante _Home Assistant Core_ gewählt. (Ein neuer Nutzer `homeassistant` wird dabei angelegt sowie ein Virtuelles Python Environment)

Zusätzlich wird noch die **Erweiterung** (Integration) für **1-Wire** benötigt:<br>
https://www.home-assistant.io/integrations/onewire/ <br>
_(Anmerkung 1: Diese Integration funktioniert auch ohne OWFS, dann jedoch nur mit Temperatursensoren)_<br>
_(Anmerkung 2: Zur Kommunikation mit OWFS nutzt die Integration ebenfalls die Pyhton Bibliothek "pyownet", wie später dann auch die Softwarekomponente für die Lichtsteuerung.)_



***
Markdown Syntax: 
https://www.markdownguide.org/basic-syntax/ <br>
Dokumentation mit Markdown-Syntax:
https://github.com/mkdocs/mkdocs <br>
Python API-Dokumentation:
https://github.com/ml-tooling/lazydocs <br>
Dokumentation veröffentlichen:
https://github.com/readthedocs/readthedocs.org