# Entwicklerwerkzeuge
Eine gute Möglichkeit zum Anpassen der Home Assistant Konfigurationen auf dem RaspPi oder auch das Entwickeln eigener Integrationen bietet *Visual Studio Code*.

## Visual Studio Code einrichten
Genereller Aufbau: Hauptrechner hat eine VS Code Installation. Mittels der Erweiterung *remote-ssh* verbindet sich VS Code mit dem RaspPi und die Programmierung / Konfiguration erfolgt direkt auf dem RaspPi.

**Schritt 1:** Erweiterung *remote-ssh* auf dem Client (Hauptrechner) installieren.<br>
**Schritt 2:** Anschließend neues Remote-Ziel hinzufügen. [Siehe Doku](https://code.visualstudio.com/docs/remote/ssh)

**Für die Arbeit mit Python:**

* "Python" extension installieren
* Wir wollen remote-ssh und virtuelle Environments nutzen!
* In VS Code verbinden wir uns mit dem remote-Rechner 
* In neuem VS Code Fenster gehen wir wieder zu Erweiterungen. Hier müssen wir die python extension für remote-rechner installieren!
* Wir öffnen einen Ordner, der unseren Workspace darstellt und erstellen ggf. eine neue "datei.py".
* Wir lassen uns ein Terminal anzeigen und erstellen ein neues virtuelles Environment: `python3.7 -m venv .venv/ow-test`
* Unten links können wir jetzt das Environment als Python interpreter auswählen und alles sollte laufen (siehe auch: https://devblogs.microsoft.com/python/remote-python-development-in-visual-studio-code/)
* **Python-Programm starten:** PLAY-Button oben rechts
* **Debugging:** F5 und "Python File" als Konfiguration und es sollte funktionieren.

