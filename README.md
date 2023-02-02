[![Documentation Status](https://readthedocs.org/projects/la-sve-home-automation/badge/?version=latest)](https://la-sve-home-automation.readthedocs.io/en/latest/?badge=latest)

# home-automation

As I don't believe, this project is of much relevance to others, it is described in German only.
It is about my personal home automation using a lot of DS18S20 temperature sensors distributed in every room of my house to control my heating system via custom made DS2408 boards connected to some finder relays that switch the underfloor heating on and off for individual rooms.
Additionally, light switches (push buttons) are used as inputs to another part of the DS2408 boards, so that they can be used normally, apart from automation via _Home Assistant_. The latter is used for automation and as a user interface. Shutter control is also realized, but with custom boards using an i2c port expander (MCP23017).

**Kurzbeschreibung:** Projektdateien zur Automatisierung eines Hauses mittels Home Assistant, RaspPi und diversen Sensoren und Aktoren auf 1-Wire Basis.

## Dokumentation
Eine [Dokumentation](docs/index.md) findet sich im `docs`-Verzeichnis.

Ebenfalls erreichbar über [readthedocs](https://la-sve-home-automation.readthedocs.io/en/latest/).
