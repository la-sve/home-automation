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

## Bedienung vereinfachen
Einige Kommandozeilenbefehle sind etwas sperrig, um sie ständig neu einzutippen.
Hier hilft die `.bashrc` weiter, in welcher aliase eingerichtet werden können.
Im Repo befindet sich darum eine Datei `.bash_aliases` im `.pi` Ordner.
Ausgehend davon, dass das home-automation Repository vom Nutzer `pi` ausgecheckt wurde, wird einfach ein Link angelegt, bspw.: 
`.bash_aliases` -> `workspace/home-automation/.pi/.bash_aliases`

## Home Assistant Config
Konfigurationsdateien (ausgenommen sensible Daten) befinden sich im `.homeassistant`-Ordner des Repositories.
Die Nutzereinstellungen und Konfigurationen der Home Assistant Installation liegen unter: `/home/homeassistant/.homeassistant/`.
Damit wir sinnvoll editieren und sichern können, kommt das ganze Verzeichnis unter Versionskontrolle. Wir haben jetzt zwei Herausforderungen: 

1. Wir wollen kein Git-Repo direkt in unserem Home, da dies ggf. mit anderen Git-Arbeitskopien in Konflikt geraten könnte und 
2. wir wollen nicht das gesamte Git-Repo auschecken, sondern nur das entsprechende Verzeichnis mit den Sicherungen für unser Home-Verzeichnis.

Folgende Vorgehensweise (als Nutzer `pi`) um einen *sparse checkout* mit git direkt in das Home-Verzeichnis durchzuführen:

* Einen Alias in `.bashrc` anlegen (sollte bereits im Vorgängerschritt erfolgt sein):
	* `alias githass='git --work-tree=/home/homeassistant --git-dir=/home/homeassistant/.home'`
	* (Wir wollen damit das Repo direkt in das Home-Verzeichnis des Nutzers `homeassistant` auschecken.)
* Wechsel in das `/home/homeassistant` Verzeichnis (Voraussetzung ist, dass Nutzer pi bereits Schreibrechte besitzt, siehe oben)
* `githass init --shared=group`
* `chgrp -R homeassistant .home`
* `githass config core.sparseCheckout true`
* `githass config core.sharedRepository true`
* `githass remote add origin git@github.com:la-sve/home-automation.git`
* `echo ".homeassistant/" >> .home/info/sparse-checkout`
* `githass fetch --depth 1 origin main`
* `githass checkout main`
* `vim .home/info/exclude`

```
# Exclude all:
/*
# Keep track:
!/.homeassistant
```

## 1-Wire Integration
Zusätzlich wird noch die **Erweiterung** (Integration) für **1-Wire** benötigt:<br>
https://www.home-assistant.io/integrations/onewire/ <br>
_(Anmerkung 1: Diese Integration funktioniert auch ohne OWFS, dann jedoch nur mit Temperatursensoren)_<br>
_(Anmerkung 2: Zur Kommunikation mit OWFS nutzt die Integration ebenfalls die Pyhton Bibliothek "pyownet", wie später dann auch die Softwarekomponente für die Lichtsteuerung.)_

## viCare Integration
Die [viCare Integration](https://www.home-assistant.io/integrations/vicare) ist standardmäßig in Home Assistant vorhanden und dient hier zum Einbinden einer **Viessmann Brennwerttherme** Vitodens 300-W mit LAN-Modul. 

Meine Erfahrungen bei der Inbetriebnahme: Der Anleitung kann gut gefolgt werden, jedoch verblieben zwei Probleme.

1. Folgende Abhängigkeit musste im venv noch installiert werden: `pip install pkce`
2. Die Integration funktionierte erst, nachdem einmalig die ViCare APP auf dem Smartphone genutzt wurde. Vorher hat die Integration kein Gerät gefunden.

Nachdem die Probleme gelöst sind, sollten neue Entitäten mit dem Namen vicare verfügbar sein.

### Hintergrundinfos
Es ist auch eine neuere Komponente in Bearbeitung, siehe, [https://github.com/oischinger/ha_vicare/tree/config_flow](https://github.com/oischinger/ha_vicare/tree/config_flow).
Um diese auszuprobieren, wird sie ausgecheckt und in `.homeassistant/custom_components` verlinkt, wie nachfolgend beschrieben:

* `su_hass`
* `cd ~`
* `mkdir hass_custom; cd hass_custom`
* `git clone --branch config_flow https://github.com/oischinger/ha_vicare.git`
* `cd ~; cd .homeassistant; mkdir custom_components`
* `ln -s ../../hass_custom/ha_vicare/custom_components/vicare`

Die vicare Integration setzt übrigens auf das Paket [PyViCare](https://github.com/somm15/PyViCare). Falls also mal etwas nicht so funktioniert, wie gedacht, kann das Paket auch unabhängig verwendet werden, um Fehler zu finden.

