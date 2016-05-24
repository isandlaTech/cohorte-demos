#!/usr/bin/python

from pelix.ipopo.decorators import ComponentFactory, Provides, Validate, Invalidate, Property
from pelix.ipopo import constants

import serial

@ComponentFactory("led_uno_wrapper_factory")
@Property("_name", "led.name", constants.IPOPO_INSTANCE_NAME)
@Property("_serial_port", "serial.port", '/dev/ttyACM0')
@Provides("java:/led.services.LedService")
class LedUnoWrapper(object):

    def __init__(self):
        self._name = "led"
        self._state = "off"
        self._serial_port = None
        self._serial = None
        
    @Validate    
    def start(self, context):
        self._serial = serial.Serial(self._serial_port, 9600)
	#self.on()

    @Invalidate    
    def stop(self, context):
        self._serial.close()
        self._serial = None
	#self.off()

    def get_name(self):
        return self._name

    def get_state(self):
        return self._state

    def on(self):             
        if self._serial.isOpen():
            self._serial.write(b"on")
            self._state = "on"
        return "on"            

    def off(self):        
        if self._serial.isOpen():
            self._serial.write(b"off")
            self._state = "off"
        return "off"

    # Java API compliance
    getName = get_name
    getState = get_state    
