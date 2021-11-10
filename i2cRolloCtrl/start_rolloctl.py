#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import time
from rolloctl.manager import RolloAutomationManager

import RPi.GPIO as GPIO
import signal
import sys, os

import json

# Daten per FLASK mit Home Assistant austauschen:
# https://realpython.com/api-integration-in-python/
# https://www.home-assistant.io/integrations/switch.rest/
# https://www.home-assistant.io/integrations/rest_command/
# https://thingsmatic.com/2017/02/07/home-assistant-integrating-restful-switches/

# Script als systemd Service ausführen, siehe:
#   https://github.com/torfsen/python-systemd-tutorial

from flask import Flask, request, jsonify
app = Flask(__name__)
        


def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)

# @app.route("/Shutters/<int:moduleNumber>/<int:pinNumber>", methods=["GET"])
# def get_shutters(moduleNumber, pinNumber):
#     #state = manager.state(moduleNumber,pinNumber)
#     #return ('on' if state else 'off')
#     return 50

@app.route("/Shutters",methods=["PUT","POST"])
def update_shutter_state():
    state=None
    print(request)
    if request.json is not None:
        window = int(request.json.get("window"))
        cmd = request.json.get("cmd")
        print(request.json)
        if ('time' in request.json) and request.json.get("time"):
            time = int(request.json.get("time"))
            print(f"Requested window {window} with command {cmd} and time {time}")
            state = manager.activate(window, cmd, time)
        else:
            print(f"Requested window {window} with command {cmd}")
            state = manager.activate(window, cmd)
    else:
        print("Only json formatted post requests are supported!")
        state = request.data.decode("utf-8")

    return state, 201

if __name__ == "__main__":

    # TODO: Einstellungsdatei per command line argument!

    # Einstellungen aus json-Datei laden
    f = open(os.path.join(sys.path[0],'config','manager_test.json'))
    settings = json.load(f)
    f.close()

    # Interrupt-Pin am Raspberry Pi, welcher mit Interrupt-Leitung der Rollo-Module verbunden ist.
    interrupt_gpio = settings["interrupt_gpio"]

    manager = RolloAutomationManager(settings["modules"], interrupt_gpio = interrupt_gpio)
    app.debug = False
    app.use_reloader = False

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(interrupt_gpio, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(interrupt_gpio, GPIO.FALLING, 
            callback=manager.newInputDetected)  #, bouncetime=10

    try:
        manager.start()
        threading.Thread(target=lambda: app.run(host="0.0.0.0",port=5000)).start()
        while True:
            time.sleep(10)
            print('MainLoop')
    except (KeyboardInterrupt, SystemExit):
        manager.running = False
        manager.join()
        GPIO.cleanup()
        sys.exit(0)

