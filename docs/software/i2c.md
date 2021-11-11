# Rollo Module per I2C einbinden

Für die Ansteuerung der MCP23017-Module wurde ein Python-Skript geschrieben. 
Wir müssen hier mit einem separatem Skript arbeiten, da wir möglichst schnell auf Änderungen der Eingangsports reagieren wollen, d.h. sobald ein Taster eines Rollos gedrückt wurde. 
Das erstellte Skript reagiert per Interrupt auf dem Raspberry Pi auf das Interrupt-Signal der MCP23017-Module. 
Hierbei teilen sich alle an einem i2c-Bus befindlichen MCP23017-Module ein Signalkabel.
Es ist also nicht ersichtlich, welches Modul den Interrupt ausgelöst hat. 
Sobald ein Interrupt auftrat, werden die Zustände der einzelnen Rollo-Ansteuerungen geprüft und ggf. aktualisiert. 
Zusätzlich findet diese Aktualisierung in einem Zeitintervall von 1 Sekunde statt. 
Bei dieser regelmäßigen Aktualisierung werden jedoch die Eingangsports nicht neu eingelesen.
Neben der Steuerung der Rollos per Taster, stellt das Python-Skript eine einfach, per flask implementierte REST API bereit. 
D.h. von Außen können über den Port 5000 ebenfalls Rollo-Kommandos vorgegeben werden.
Dieses Interface wird auch genutzt, um die Rollos per Home Assistant zu steuern.

In Home Assistent wird dazu die ["RESTful Command" Integration](https://www.home-assistant.io/integrations/rest_command/) verwendet sowie das [Template "Cover"](https://www.home-assistant.io/integrations/cover.template) zur Integration in die Oberfläche.

**ACHTUNG:** Für die Verwendung des Moduls muss das I2C-Interface auf dem Raspberry Pi (bspw. über `raspi-config`) aktiviert werden.

Das Skript sollte als `systemd`-Service eingerichtet werden. Nähere Informationen hierzu sind in der Beschreibung des Python-Moduls beschrieben.