# 1-Wire einrichten und konfigurieren

## 1-Wire Bus per GPIO auf RaspPi

-   Über `raspi-config` wird zunächst das 1-Wire Interface aktiviert.
-   Jetzt muss noch der zu verwendende Pin angegeben werden:<br>
    `> sudo vim /boot/config.txt`<br>
    
    > dtoverlay=w1-gpio,gpiopin=21 #DS2408 devices,  4.7kOhm external Pull-Up <br>
    > dtoverlay=w1-gpio,gpiopin=4 #DS18S20 temp devices, 1st bus 1.5kOhm external Pull-Up<br>
    > dtoverlay=w1-gpio,gpiopin=13 #DS18S20 temp devices, 2nd bus 1.5kOhm external Pull-Up<br>
    > dtoverlay=w1-gpio,gpiopin=26 #DS18S20 temp devices, 3rd bus 1.5kOhm external Pull-Up<br>
    > dtoverlay=w1-gpio,gpiopin=27 #DS18S20 temp devices, 4th bus 1.5kOhm external Pull-Up<br>
    
-   REBOOT

Die funktionsweise kann wie folgt geprüft werden _(Hier wurde ein DS18S20 und DS2408 angeschlossen.)_:<br>
    `> lsmod | grep -i w1_`
    
```
w1_ds2408              16384  0
w1_therm               28672  0
w1_gpio                16384  0
wire                   36864  3 w1_gpio,w1_ds2408,w1_therm
```

Weitere Informationen finden sich bspw. auch [hier](https://pinout.xyz/pinout/1_wire#)

## OWFS (1-Wire File System)
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