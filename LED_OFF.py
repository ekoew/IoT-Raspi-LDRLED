#!/usr/bin/env python
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

print "Lampu dimatikan"
GPIO.output(18,GPIO.LOW)