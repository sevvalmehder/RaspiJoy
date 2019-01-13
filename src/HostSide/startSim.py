import sys
import os

# Keep available joystick list in dictionary
availableJSs = {
	0 :	"RaspiJoy",
	1 : "Cypress USB dsmX HID",
	2 : "Great Planes GP Controller",
	3 : "*SAILI Simulator*",
	4 : "Sony PLAYSTATION(R)3 Controller",
	5 : "Microsoft X-Box 360 pad"
}

if __name__ == '__main__':
	# Write down the available joysticks
	print('Welcome\nAvailable joysticks for RaspiJoy:')
	for x in availableJSs:
		print('({}) {}'.format(x, availableJSs[x]))

	# Get user input
	print("Select a joystick")
	choice = sys.stdin.readline()

	# Write user input
	with open('js.usr','w') as f:
		f.write("{}".format(choice))

	print("Simulator starting..")



	try:
		# Read user input
		with open('js.usr','r') as f:
			choice = int(f.read())

	# If file doesnt exist, the program was started normally
	# So we use joystick as a RaspiJoy
	except:
		choice = 0




	os.system("sim_vehicle.py -v ArduCopter -f gazebo-iris --consol --map")