# Home Assistant
Hier kann der offiziellen Anleitung gefolgt werden. Dabei wird die Variante _Home Assistant Core_ gewählt. (Ein neuer Nutzer `homeassistant` wird dabei angelegt sowie ein Virtuelles Python Environment)

Für späteres komfortables Arbeiten, wird der Nutzer `pi` in die Gruppe `homeassistant` aufgenommen (`vim /etc/group`) und die Gruppenschreibrechte im `/home/homeassistant`-Verzeichnis werden entsprechend gesetzt: `sudo chmod -R g+w .homeassistant/`

## (optional) Aktuelles Python
Ggf. benötigt die aktuellste Home Assistant Version eine neuere Python-Version als die verwendete Linux-Distribution zur Verfügung stellt. Dann muss eine aktuelle Python-Version manuell installiert werden. Diese existiert dann typischerweise parallel zur vorhandenen.

- `sudo apt update`
- `sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libsqlite3-dev libreadline-dev libffi-dev curl libbz2-dev`
- [Release für nachfolgendes Kommando raussuchen](https://www.python.org/downloads/source/)
- `curl -O https://www.python.org/ftp/python/3.8.12/Python-3.8.12.tar.xz`
- `tar -xf Python-3.8.12.tar.xz`
- `cd Python-3.8.12`
- `./configure --enable-optimizations`
- `make -j 4`
- `sudo make altinstall`

Damit steht das Binary `python3.8` zur Verfügung.

## Autostart
Home Assistant sollte als *systemd* Service eingerichtet werden. Die [entsprechende Dokumentation](https://www.home-assistant.io/docs/autostart/systemd/) gibt Aufschluss über das Vorgehen.

Nach erfolgreicher Einrichtung sind folgende Befehle relevant:

- Start: `sudo systemctl start home-assistant@homeassistant.service`
- Neustart: `sudo systemctl start home-assistant@homeassistant.service`
- Logging Output: `sudo journalctl -f -u home-assistant@homeassistant.service`


## 1-Wire Integration
Zusätzlich wird noch die **Erweiterung** (Integration) für **1-Wire** benötigt:<br>
https://www.home-assistant.io/integrations/onewire/ <br>
_(Anmerkung 1: Diese Integration funktioniert auch ohne OWFS, dann jedoch nur mit Temperatursensoren)_<br>
_(Anmerkung 2: Zur Kommunikation mit OWFS nutzt die Integration ebenfalls die Pyhton Bibliothek "pyownet", wie später dann auch die Softwarekomponente für die Lichtsteuerung.)_


