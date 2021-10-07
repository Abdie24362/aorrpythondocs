#A. Rosario Rodriguez
#Lists Practice 1

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)

import time
#A variable that holds more than one value is a list.
Funny = ['funny quote 1', 'funny quote 2', 'funny quote 3', 'funny quote 4']
import random
x = random.randint(0, 3)

while True:
    time.sleep(1)
    if GPIO.input(6) == GPIO.LOW :
        print(Funny[x])
    