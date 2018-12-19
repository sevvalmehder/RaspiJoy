# Locate the YAML file
MAVProxy loads joystick definitions dynamically from YAML
files, which makes it easier for someone to add support for a device
without needing to patch mavproxy itself.  

A joystick definition([RaspiJoy.yml](https://github.com/sevvalmehder/RaspiJoy/blob/master/src/HostSide/RaspiJoy.yml)) be located either inside the MAVProxy python module in the joysticks directory.

# For starting simulator

1) Open a terminal and go to the Gazebo directory
```
	$ cd ~/ardupilot_gazebo
```

2) Launch Gazebo with demo 3DR model
```
	$ gazebo --verbose worlds/iris_arducopter_runway.world
```
3) Open a new terminal and go to ArduCopter directory

```
	$ cd ~/ardupilot/ArduCopter
```

4) Reload the path (log-out and log-in to make permanent)
```
	$ . ~/.profile
```

5) Start SITL using --map and --console options
```
	$ sim_vehicle.py -v ArduCopter -f gazebo-iris --map --console
```

# Load the joystick
```
	$ module load joystick
```

