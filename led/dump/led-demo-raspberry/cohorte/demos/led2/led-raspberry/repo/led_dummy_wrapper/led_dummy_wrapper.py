#!/usr/bin/python

from pelix.ipopo.decorators import ComponentFactory, Provides, Validate, Invalidate, Property
from pelix.ipopo import constants

@ComponentFactory("led_dummy_wrapper_factory")
@Property("_name", "led.name", "dummy-led")
@Provides("java:/led.services.LedService")
class LedDummyWrapper(object):

    def __init__(self):
        self._name = "led"
        self._state = "on"
        
    @Validate    
    def start(self, context):
        self.on()

    @Invalidate    
    def stop(self, context):
        self.off()

    def get_name(self):
        return self._name

    def get_state(self):
        return self._state

    def on(self):             
        self._state = "on"            

    def off(self):        
        self._state = "off"

    # Java API compliance
    getName = get_name
    getState = get_state    