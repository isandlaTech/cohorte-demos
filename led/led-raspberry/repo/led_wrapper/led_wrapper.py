#!/usr/bin/python

from pelix.ipopo.decorators import ComponentFactory, Provides, Validate, Invalidate, Property
from pelix.ipopo import constants

import serial

@ComponentFactory("led_wrapper_factory")
@Property("_name", "led.name", constants.IPOPO_INSTANCE_NAME)
@Property("_serial_port", "serial.port", '/dev/tty.usbmodem1d1131')
@Provides("java:/led.services.LedService")
class LedWrapper(object):

    def __init__(self):
        self._name = "led"
        self._state = "on"
        self._serial_port = None
        self._serial = None
        
    @Validate    
    def start(self, context):
        self._serial = serial.Serial(self._serial_port, 9600, timeout=5)
        self.on()

    @Invalidate    
    def stop(self, context):
        self._serial.close()
        self._serial = None
        self.off()

    def get_name(self):
        return self._name

    def get_state(self):
        return self._state

    def on(self):             
        if self._serial.isOpen():
            self._serial.write("on")
            self._state = "on"            

    def off(self):        
        if self._serial.isOpen():
            self._serial.write("off")
            self._state = "off"

    # Java API compliance
    getName = get_name
    getState = get_state    