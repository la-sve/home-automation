# Software

## Beispiel Einrichtung RaspPi

**System:** Raspbian GNU/Linux 11 (bullseye) 
**Stand:** Dezember 2022

### SD-Karte vorbereiten
Da eine *Headless*-Installation durchgeführt wird, erfolgt die Systeminstallation wie folgt:

* Installation von *Raspberry Pi Imager*
* SD-Karte einlegen und mit System bespielen
* SD-Karte mounten
    * boot-Partition: `ssh`-Datei anlegen
    * boot-Partition: `userconf`-Datei anlegen. Inhalt ist `<username>:<pass>`. Das Passwort kann bspw. auf einem Raspbian System wie folgt generiert werden: `'mypassword' | openssl passwd -6 -stdin`
    * root-fs-Partition: Hostname in `/etc/hostname` anpassen

### System aktualisieren
(Achtung kann eine Weile dauern)
```bash
sudo apt-get update
sudo apt-get upgrade
sudo reboot  #bei kernel aktualisierung
```

### Docker installieren
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker lasve
# LOG OUT AND LOGIN AGAIN
docker version  #-> Zur Info
```

### Docker Compose installieren
```bash
sudo apt install docker-compose-plugin
sudo systemctl enable docker
```

### home-automation einrichten
```bash
ssh-keygen -t ed25519 -C "MAILADR"
cat /home/lasve/.ssh/id_ed25519.pub  #SCHLÜSSEL bei Github eintragen

mkdir workspace
cd workspace
git clone git@github.com:la-sve/home-automation.git
cd ~
ln -s workspace/home-automation/.pi/.bash_aliases .bash_aliases
```

Die Daten von Home Assistant können vom alten Rechner oder Backup bspw. einfach mittels FreeFileSync übernommen werden.

### i2c aktivieren
Prinzipiell nur über `sudo raspi-config` aktivieren. 

### Rollos (Python Service)
Details zur Rolloansteuerung in der Rubrik [i2c](software/../i2c.md). Sowie der [Projektseite](https://github.com/la-sve/home-automation/tree/main/i2cRolloCtrl).

### Onewire aktivieren
Zunächst muss w1 als Kernelmodul entsprechend aktiviert und konfiguriert werden. Darauf aufbauend kommt noch das One-Wire File System (owfs) zum Einsatz. Details siehe [OneWire](software/../oneWire.md).

### MQTT Broker 
Wird u.a. für das Einbinden der Tasmota-Steckdosen in HomeAssistant benötigt.

```bash
sudo apt update && sudo apt install -y mosquitto mosquitto-clients
# Passwort und Zugang einrichten
sudo mosquitto_passwd -c /etc/mosquitto/passwd your_username
sudo vim /etc/mosquitto/conf.d/default.conf
> listener 1883
> allow_anonymous false
> password_file /etc/mosquitto/passwd
# Als Service aktivieren
sudo systemctl restart mosquitto
sudo systemctl enable mosquitto
# Fehlersuche:
journalctl --unit=mosquitto -f
```

### Homeassistant
Entgegen der Seite [Home Assistant](software/../hass.md) wird hier auf Docker zurückgegriffen, was die Installation und Wartung vereinfachen sollte. 

```bash
cd workspace/home-automation/docker/homeassistant
docker compose up -d   # Kann auch zum Neubauen des Containers genutzt werden
```