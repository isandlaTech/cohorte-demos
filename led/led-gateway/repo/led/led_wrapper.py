#!/usr/bin/python

from pelix.ipopo.decorators import ComponentFactory, Provides, Validate, Invalidate

import serial

@ComponentFactory("led_wrapper_factory")
@Provides("led.service")
class LedWrapper(object):

    def __init__(self):
        self._state = "off"
        self._serial = None
        
    @Validate    
    def start(self, context):
        self._serial = serial.Serial('/dev/tty.usbmodem1d1131', 9600, timeout=5)

    @Invalidate    
    def stop(self, context):
        self._serial.close()
        self._serial = None

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
