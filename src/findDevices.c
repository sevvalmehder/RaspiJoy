// How to compile?
// gcc findDevices.c `pkg-config --libs libusb-1.0` -o exe

#include <stdio.h>
#include <errno.h> // For errno
#include <stdbool.h> // For bool
#include <stdlib.h> // For malloc
#include <libusb-1.0/libusb.h>


#define VENDOR_ID 0x13d3
#define PRODUCT_ID 0x3402

/*
 * Get a list of USB devices
 * Parameter: 
 * 		list: output location for a list of devices
 * Return:
 * 		number of devices & size of output list
 */
int getAllDevices(libusb_device ***list);

/*
 * Search all device and find given VID and PID
 * Parameter:
 * 		vID: vendor ID of device
 * 		pID: product ID of device
 * 		dev: location of device
 * 		devices: list of devices
 * Return:
 *		true if found, false otherwise
 */
bool recognizeDevice(uint16_t vID, uint16_t pID, libusb_device **devices);

int main(){

	// Device list
	libusb_device **devs;
	// Count of the devices
	size_t count;
	// Return value
	int r;
	// Is device exist?
	bool isExist;

	// Call the initialize function
	if( LIBUSB_SUCCESS != libusb_init(NULL))
		return r;

	// Get the devices
	count = getAllDevices(&devs);
	if( count < 0)
		return count;

	// Get memory for device and call search function
	isExist = recognizeDevice(VENDOR_ID, PRODUCT_ID, devs);
	
	if(isExist)
		printf("We found the device[vendor ID: %x, product ID: %x]\n", VENDOR_ID, PRODUCT_ID);
	else
		printf("Device cant found :(\n");

	// Frees a list of device previously discovered using get_device_list()
	// unref_devices parameter sets 1
	// this means the reference count of each device in the list is decremented by 1
	libusb_free_device_list(devs, 1);


	// Deinitialize libusb 
	// Should be called before termination
	libusb_exit(NULL);

	return 0;
}

int getAllDevices(libusb_device ***list){

	// Number of devices
	int count;

	count = libusb_get_device_list(NULL, list);
	
	return (int)count;

}

bool recognizeDevice(uint16_t vID, uint16_t pID, libusb_device **devices){

	// Loop control variable
	int i = 0;
	// Device descriptor struct
	struct libusb_device_descriptor sDev;
	// Return value
	int r;

	libusb_device *device;
	while( (device = devices[i++]) != NULL){

		
		libusb_device_handle *handle = NULL;

		// This is a nonblocking function
		// Device descriptor is cached in memory.
		// It returns 0 on success
		r = libusb_get_device_descriptor(device, &sDev);
		if(LIBUSB_SUCCESS != r){
			fprintf(stderr, "failed to get devide descriptor\nValue of errno: %d\n", errno);
			return false;
		}

		if(vID == sDev.idVendor && pID == sDev.idProduct){
			return true;
		}
	}
	return false;
}
