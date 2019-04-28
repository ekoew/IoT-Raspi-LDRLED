#!/usr/bin/env python
import time
import RPi.GPIO as GPIO
from gpiozero import LightSensor, Buzzer

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

ldr = LightSensor(4)
while True:
    if ldr.value==0:
        print("TIDAK ADA CAHAYA")
        print "Lampu dihidupkan"
        GPIO.output(18,GPIO.HIGH)
    elif ldr.value>0 and ldr.value<=0.2:
        print("CAHAYA REDUP")
        print "Lampu dihidupkan"
        GPIO.output(18,GPIO.HIGH)
    elif ldr.value>0.2 and ldr.value<=0.4:
        print("CAHAYA SEDANG")
        print "Lampu dimatikan"
        GPIO.output(18,GPIO.LOW)
    elif ldr.value>0.4 and ldr.value<=0.6:
        print("CAHAYA TERANG")
        print "Lampu dimatikan"
        GPIO.output(18,GPIO.LOW)
    elif ldr.value>0.6:
        print("CAHAYA SANGAT TERANG")
        print "Lampu dimatikan"
        GPIO.output(18,GPIO.LOW)
    print(ldr.value)
    time.sleep(1)