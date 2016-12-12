#!/usr/bin/python
###########################################
# 
# Raspberry Pi RGB Christmas Tree 
# by James Saunders
# Based on example code by Andrew Gale (www.pocketmoneytronics.co.uk)
#
# This code uses the rpi_ws281x PWM library by Jeremy Garff located at:
#    https://github.com/jgarff/rpi_ws281x
# NOTE: the library disables analogue audio out on the Pi.
#
# LED arrangement:         2
#                         1 3
#                        0 5 4
#
# WARNING: LEDs can be very bright. Do not set the brightness too high. 
# Avoid looking directly at the LEDs.
#
###########################################

from random import randint
from time import sleep
from neopixel import *

# Setup
LED_COUNT      = 6
LED_PIN        = 18
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_INVERT     = False   # True to invert the signal
LED_BRIGHTNESS = 50      # Set to 0 for darkest and 255 for brightest

tree = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
tree.begin()

colours = ['red', 'blue', 'magenta', 'cyan', 'yellow', 'green']

####################
# Useful Functions
####################

# Turn all LEDs off
def all_leds_off():
	for pin in range(LED_COUNT):
		set_led_rgb(pin, 0, 0, 0)
	tree.show()
	return                             

# Turn all LEDs on
def all_leds_on():
	for pin in range(LED_COUNT):
		set_led_rgb(pin, 255, 255, 255)
	tree.show()                               
	return
 
# Set a specified LED a colour (by by RGB)
def set_led_rgb(led, red, green, blue):
	colour = (green & 255)<<16 | (red & 255)<<8 | (blue & 255) # Note: GRB not RGB
	tree.setPixelColor(led, colour)
	tree.show()
	return

# Set a specified LED a colour (by colour string)
def set_led_colour(led, colour):
	if   colour=="black":   set_led_rgb(led, 0, 0, 0)
	elif colour=="white":   set_led_rgb(led, 255, 255, 255)
	elif colour=="red":     set_led_rgb(led, 255, 0, 0)
	elif colour=="green":   set_led_rgb(led, 0, 255, 0)
	elif colour=="blue":    set_led_rgb(led, 0, 0, 255)
	elif colour=="yellow":  set_led_rgb(led, 255, 255, 0)
	elif colour=="cyan":    set_led_rgb(led, 0, 255, 255)
	elif colour=="magenta": set_led_rgb(led, 255, 0, 255)
	else:
		colour_error = "Unknown colour: " + colour
		print(colour_error)
	return

# Set all LEDs to the same colour (by RGB)
def set_all_rgb(red, green, blue):
	for pin in range(LED_COUNT):
		set_led_rgb(pin, red, green, blue)
	return

# Set all LEDs to the same colour (by colour string)
def set_all_colour(colour):
	for pin in range(LED_COUNT):
		set_led_colour(pin, colour)
	return


####################
# Main
####################
while True:

	## EXAMPLE 1: Flash some colours (all LEDs the same colour)
	all_leds_off()
	for colour in colours:
		set_all_colour(colour)
		sleep(0.5)
	all_leds_off()


	## EXAMPLE 2: Cycle through the colours in turn
	all_leds_off()
	for colour in colours:
		for led in range(LED_COUNT):
		    set_led_colour(led, colour)
		    sleep(0.3)
	all_leds_off()


	## EXAMPLE 3: Sweep green/red up from the bottom
	all_leds_off()
	set_all_colour("green")
	sleep(0.4)
	for i in range(3):
		# sweep-up in RED
		set_led_colour(0, "red")
		set_led_colour(5, "red")
		set_led_colour(4, "red")
		sleep(0.4)
		set_led_colour(1, "red")
		set_led_colour(3, "red")
		sleep(0.4)
		set_led_colour(2, "red")
		sleep(0.4)
		# sweep-up in YELLOW
		set_led_colour(0, "green")
		set_led_colour(5, "green")
		set_led_colour(4, "green")
		sleep(0.4)
		set_led_colour(1, "green")
		set_led_colour(3, "green")
		sleep(0.4)
		set_led_colour(2, "green")
		sleep(0.4)
	all_leds_off()


	## EXAMPLE 4: Some pulsing of the colour
	all_leds_off()
	for red in range(255):
		set_all_rgb(red, 0, 0)   # Ramp-up the RED
		sleep(0.005)
	for green in range(255):
		set_all_rgb(0, green, 0) # Ramp-up the GREEN
		sleep(0.005)
	for blue in range(255):
		set_all_rgb(0, 0, blue)  # Ramp-up the BLUE
		sleep(0.005)
	all_leds_off()


	## EXAMPLE 5: Some randomness
	all_leds_off()
	# Start off in a random state
	for led in range(LED_COUNT):
		red   = randint(0, 255)
		green = randint(0, 255)
		blue  = randint(0, 255)
		set_led_rgb(led, red, green, blue)
	# Now randomly choose an LED and set it to a random colour
	for i in range(50):
		led   = randint(1, 6)
		red   = randint(0, 255)
		green = randint(0, 255)
		blue  = randint(0, 255)
		set_led_rgb(led, red, green, blue)
		sleep(0.3)
	all_leds_off()

