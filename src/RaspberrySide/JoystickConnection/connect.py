#!/usr/bin/python

import RPi.GPIO as GPIO
import spidev
import os
import time

#
# Define channels
#
# Left joystick(below one) horizantal movement channel
ch_l_joystick_hor = 0
# Left joystick(below one) vertex movement channel
ch_l_joystick_ver = 1
# Right joystick(upper one) horizantal movement channel
ch_r_joystick_hor = 6
# Right joystick(upper one) vertex movement channel
ch_r_joystick_ver = 7

# Set raspberry pi pins
GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Assign buttons to the variables
right_button = GPIO.input(2)
top_button = GPIO.input(3)
left_button = GPIO.input(4)
bottom_button = GPIO.input(17)

# Delay in seconds
delay = 0.1

# SPI constants
spi_port = 0
spi_device = 0

# Create spi object
spi = spidev.SpiDev()
spi.open(spi_port, spi_device)

def readChannel(channel):
	# read SPI data from MCP3008 channel
	r = spi.xfer2([1, 8 + channel << 4, 0])
	data = ((r[1] & 3) << 8) + r[2]
	return data

def decimal2hex(num):
	# convert signed decimal number to hexadeicmal
	if number < 0:
		return hex((1 << 8) + num)
	else:
		return hex(number)

while True:
	# Read joysticks positions 
	ljs_x = readChannel(ch_l_joystick_hor)
	ljs_y = readChannel(ch_l_joystick_ver)
	rjs_x = readChannel(ch_r_joystick_hor)
	rjs_y = readChannel(ch_r_joystick_ver)

	# First 4 bit useless for buttons
	buttons = "0000"
	# Control buttons actions
	buttons = buttons + str(1) if right_button else buttons + str(0)
	buttons = buttons + str(1) if left_button else buttons + str(0)
	buttons = buttons + str(1) if top_button else buttons + str(0)
	buttons = buttons + str(1) if bottom_button else buttons + str(0)

	# Joystick will 8 byte data
	toSendData = "\{}\{}\{}\{}\{}".format(buttons,
		decimal2hex(ljs_x), decimal2hex(ljs_y), decimal2hex(rjs_x), decimal2hex(rjs_y))
	
	# print(toSendData)
	
	# wait 
	time.sleep(delay)