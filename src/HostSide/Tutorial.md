# Locate the YAML file
MAVProxy loads joystick definitions dynamically from YAML
files, which makes it easier for someone to add support for a device
without needing to patch mavproxy itself.  

A joystick definition([RaspiJoy.yml](https://github.com/sevvalmehder/RaspiJoy/blob/master/src/HostSide/RaspiJoy.yml)) be located either inside the MAVProxy python module in the joysticks directory.

# Modify the joystick mode init file 
MAVProxy uses __init__.py file to load joysticks. RaspiJoy has a option that use the definition of other well-known joysticks. Because of this feature this init file must be modified. The modified init file([__init__.py](https://github.com/sevvalmehder/RaspiJoy/blob/master/src/HostSide/__init__.py)) be located either inside the MAVProxy python module in the mavproxy_joystick directory.

# For starting simulator

1) Open a terminal and go to the Gazebo directory
```
	$ cd ~/ardupilot_gazebo
```

2) Launch Gazebo with demo 3DR model
```
	$ gazebo --verbose worlds/iris_arducopter_runway.world
```

3) Reload the path (log-out and log-in to make permanent)
```
	$ . ~/.profile
```
4) Execute startSim.py python file to make joystick selection and start the SITL
```
	$ python startSim.py
```

# Load the joystick

When SITL running, load joystick using MAVProxy command
```
	$ module load joystick
```
# Simulation
One of the buttons control the arm/disarm function. To use this function, the value of RC7_OPTION parameter must be 41. Run this command on simulation program:
```
	> param set RC7_OPTION 41
```
More functions can be assigned this button. All this functions were contained in the [Complete Parameter List Documentation](http://ardupilot.org/copter/docs/parameters.html#ch7-opt-channel-7-option).


