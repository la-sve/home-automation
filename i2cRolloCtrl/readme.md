# I2C Rollo Controller
Hilfsprogramm zum Ansteuern der Rollos über einen MCP23017 Schaltkreis.

## Installationsmöglichkeit
Aus diesem Ordner heraus:
> `pip3 install -e . --user`

-> erzeugt nur einen Link im entsprechenden Python Package-Path. Dieser kann über folgenden Befehl herausgefunden werden: `python3 -m site --user-site`

Deinstallieren mit:
> `pip uninstall .`

Quelle: https://python-102.readthedocs.io/en/latest/packaging.html

## Als Nutzer-Service für systemd einrichten
(siehe: https://github.com/torfsen/python-systemd-tutorial)

Service-Konfigurationsdatei aus `config/*.service` in folgendes Verzeichnis kopieren oder verlinken:
> `~/.config/systemd/user/`

Anschließend Services aktualisieren:
> `systemctl --user daemon-reload`

Weitere wichtige Befehle:
> `systemctl --user start rolloctl.service` <br>
> `systemctl --user status rolloctl.service` <br>
> `journalctl --user-unit rolloctl.service`

Automatisch mit Systemstart starten:
> `sudo loginctl enable-linger $USER` <br>
> `systemctl --user enable rolloctl.service`