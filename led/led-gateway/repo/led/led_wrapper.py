#!/usr/bin/python

from pelix.ipopo.decorators import ComponentFactory, Provides, Validate, Invalidate

import logging

import serial

_logger = logging.getLogger(__name__)

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
        _logger.critical(">>>>>> sending ON") 
        if self._serial.isOpen():
            self._serial.write("on")
            self._state = "on"
            _logger.critical(">>>>>> ON sent")   
        else:
            _logger.critical(">>>>>> Serial is not open!")   

    def off(self):        
        _logger.critical(">>>>>> sending OFF") 
        if self._serial.isOpen():
            self._serial.write("off")
            self._state = "off"
            _logger.critical(">>>>>> OFF sent")   
        else:
            _logger.critical(">>>>>> Serial is not open!")   