#!/usr/bin/python
###########################################
# 
# Raspberry Pi Snowman
# by James Saunders
# Based on example code from Tony Goodhew (https://wiki.ryanteck.uk)
#
# This program runs different LED patterns on the Ryanteck Pi Snowman.
# 
# LED arrangement:
#     Left Buttons: LED01 = Pin 07, LED02 = Pin 08, LED3 = Pin 09
#    Right Buttons: LED04 = Pin 22, LED05 = Pin 18, LED6 = Pin 17
#             Eyes: LED08 = Pin 23, LED09 = Pin 24
#             Nose: LED07 = Pin 25
#
###########################################

import random
import time
import RPi.GPIO as GPIO

LEDs = [7, 8, 9, 22, 18, 17, 23, 24, 25]
EYE_LEFT  = 23
EYE_RIGHT = 24
NOSE = 25

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
for n in LEDs:
	GPIO.setup(n, GPIO.OUT)
pwmLED = GPIO.PWM(NOSE, 200)
pwmLED.start(0)


####################
# Useful Functions
####################

# Turn all LEDs off
def all_leds_off():
	for i in LEDs:
		GPIO.output(i, False)
	return
	pwmLED.ChangeDutyCycle(0)

# Turn all LEDs on
def all_leds_on():
	for i in LEDs:
		GPIO.output(i, True)
	return
	pwmLED.ChangeDutyCycle(100)

# Spin Clockwise
def spin_clockwise():
	for i in range(6):
		GPIO.output(LEDs[i], False)
	for spin in range(5):
		for i in range(5, -1, -1):
			GPIO.output(LEDs[i], True)
			time.sleep(0.07)
			GPIO.output(LEDs[i], False)
	for i in range(6):
		GPIO.output(LEDs[i], True)
	return

# Wobble Side to Side
def wobble():
	for i in range(6):
		GPIO.output(LEDs[i], False)
	for i in range(6):
		GPIO.output(7, True)
		GPIO.output(8, True)
		GPIO.output(9, True)
		time.sleep(0.1)
		GPIO.output(7, False)
		GPIO.output(8, False)
		GPIO.output(9, False)
		time.sleep(0.1)
		GPIO.output(22, True)
		GPIO.output(18, True)
		GPIO.output(17, True)
		time.sleep(0.1)
		GPIO.output(22, False)
		GPIO.output(18, False)
		GPIO.output(17, False)
		time.sleep(0.1)
	for i in range(6):
		GPIO.output(LEDs[i], True)
	return

# Fade Nose
def nose_fade_in():
	for brightness in range(0, 100, 5):
		pwmLED.ChangeDutyCycle(brightness)
		time.sleep(0.3)

# Wink Left Eye
def eye_wink():
	GPIO.output(EYE_LEFT, True)
	GPIO.output(EYE_RIGHT, True)
	time.sleep(1)
	GPIO.output(EYE_LEFT, False)
	time.sleep(1)
	GPIO.output(EYE_LEFT, True)
	GPIO.output(EYE_RIGHT, True)
	time.sleep(1)
	return

# Up and Down
def up_down():
	for i in range(6):
		GPIO.output(LEDs[i], False)
	for i in range(4):
		for n in range(3):
			GPIO.output(LEDs[n], True)
			GPIO.output(LEDs[5-n], True)
			time.sleep(0.1)
			GPIO.output(LEDs[n], False)
			GPIO.output(LEDs[5-n], False)
			time.sleep(0.1)
		for m in range(3):
			n = 2-m
			GPIO.output(LEDs[n], True)
			GPIO.output(LEDs[5-n], True)
			time.sleep(0.1)
			GPIO.output(LEDs[n], False)
			GPIO.output(LEDs[5-n], False)
			time.sleep(0.1)    
	for i in range(6):
		GPIO.output(LEDs[i], True) # White ON
	return

####################
# Main
####################

while True:
	all_leds_off()
	nose_fade_in()
	eye_wink()
	wobble()
	spin_clockwise()
	eye_wink()
	up_down()
