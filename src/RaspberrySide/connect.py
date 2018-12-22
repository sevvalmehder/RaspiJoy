#!/usr/bin/python
import time

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

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

# Delay in seconds
delay = 0.5

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

	# Joystick will send 5 byte data
	toSendData = chr(127) + chr(ljs_x) + chr(ljs_y) + chr(rjs_x) + chr(rjs_y)
	
	# Send the data 
	writeReport(toSendData)

	# wait 
	time.sleep(delay)
