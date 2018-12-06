#!/usr/bin/python

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

	# Joystick will 8 byte data
	toSendData = "\{x00}\{}\{}\{}\{}".format(
		decimal2hex(ljs_x), decimal2hex(ljs_y), decimal2hex(rjs_x), decimal2hex(rjs_y))
	
	# print(toSendData)
	
	# wait 
	time.sleep(delay)