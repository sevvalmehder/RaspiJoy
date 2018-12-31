#!/usr/bin/python
import time

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
# Import GPIO
import RPi.GPIO as GPIO

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# GPIO setup for buttons
GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#
# Define channels
#
# Left joystick(below one) horizantal movement channel
ch_leftJS_hor = 0
# Left joystick(below one) vertex movement channel
ch_leftJS_ver = 1
# Right joystick(upper one) horizantal movement channel
ch_rightJS_hor = 6
# Right joystick(upper one) vertex movement channel
ch_rightJS_ver = 7

#
# Define buttons value
# This values effect the data to be sent 
# For example when just button3 pressed, joystick will send 4
# When both button3 and button4 pressed, js will send 12
val_but1 = 1
val_but2 = 2
val_but3 = 4
val_but4 = 8

# Keep button 1 pressed value
but4Pressed = False

# Delay in seconds
delay = 0.1

def readChannel(channel):
	# read SPI data from MCP3008 given channel and divide by 2^3 because 
	# 7 byte data will send except sign bit but the readed data is 10 byte
	return mcp.read_adc(channel)/8

def writeReport(report):
	with open('/dev/hidg0', 'rb+') as fd:
		fd.write(report.encode())

while True:
	# Read joysticks positions from channels
	ljs_x = readChannel(ch_leftJS_hor)
	ljs_y = readChannel(ch_leftJS_ver)
	rjs_x = readChannel(ch_rightJS_hor)
	rjs_y = readChannel(ch_rightJS_ver)

	buttonInfo = 0;
	# Control the buttons
	if not GPIO.input(23):
		buttonInfo += val_but1
	if not GPIO.input(24): 
		buttonInfo += val_but2
	if not GPIO.input(25):
		buttonInfo += val_but3
	if not GPIO.input(12):
		# If not pressed button4, press
		# If pressed, release
		if not but4Pressed:
			but4Pressed = True
		else:
			but4Pressed = False
		buttonInfo += val_but4

	# If button4 already pressed, add the value of button4
	if but4Pressed:
		buttonInfo += val_but4
		
	# Joystick will send 5 byte data
	toSendData = chr(buttonInfo) + chr(ljs_x) + chr(ljs_y) + chr(rjs_x) + chr(rjs_y)
	
	# Send the data 
	writeReport(toSendData)

	# wait
	time.sleep(delay)