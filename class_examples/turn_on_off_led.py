#!/usr/bin/env python
# this script turns the Auto Flash LED on and then off

import RPi.GPIO as GPIO
import time

# breadboard setup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# assign pin number for Auto Flash LED;  pin 11 = GPIO 17
led_pin = 11

# set Auto Flash LED pin's mode as output
GPIO.setup(led_pin,GPIO.OUT)

# turn on Auto Flash LED
GPIO.output(led_pin,True)
time.sleep(2)

# turn off Auto Flash LED
GPIO.output(led_pin,False)

# reset GPIO resources used by script
GPIO.cleanup()
