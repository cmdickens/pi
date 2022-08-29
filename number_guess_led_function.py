#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import random

# breadboard setup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# assign pin number for LED;  pin 11 = GPIO 17
led_pin = 11

# set LED pin's mode as output
GPIO.setup(led_pin,GPIO.OUT)

# generate a random number from 1 to 10
n = random.randint(1,10)

def flash_led():
    # turn on LED
    GPIO.output(led_pin,True)

    time.sleep(2)

    # turn off LED
    GPIO.output(led_pin,False)

# keep running until number is guessed
while True:
    print ('Guess of a number from 1 to 10')
    guess = raw_input()
    guess = int(guess)
    if guess < n:
        print "guess is too low"
    elif guess > n:
        print "Guess is too high"
    else:
        print "you guessed it"
        flash_led()
        break

# reset GPIO resources used by script
GPIO.cleanup()
