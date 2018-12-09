# For starting simulator

1) Go to the ArduCopter directory
```
	$ cd ~/ardupilot/ArduCopter
```

2) Reload the path (log-out and log-in to make permanent)
```
	$ . ~/.profile
```

3) Start SITL using --map and --console options
```
	$ sim_vehicle.py --map --console
```
# Locate the YAML file
MAVProxy loads joystick definitions dynamically from YAML
files, which makes it easier for someone to add support for a device
without needing to patch mavproxy itself.  

A joystick definition([RaspiJoy.yml](https://github.com/sevvalmehder/RaspiJoy/blob/master/src/HostSide/RaspiJoy.yml)) be located either inside the MAVProxy python module in the joysticks directory.

# Load the joystick
```
	$ module load joystick
```

