#!/usr/bin/python

from pelix.ipopo.decorators import ComponentFactory, Provides, Validate, Invalidate, Property
from pelix.ipopo import constants

import pifacedigitalio
#import time

@ComponentFactory("led_piface_wrapper_factory")
@Property("_name", "led.name", constants.IPOPO_INSTANCE_NAME)
@Provides("java:/led.services.LedService")
class PiFaceWrapper(object):

    def __init__(self):
        self._name = "led"
        self._state = "off"
        self._pif = pifacedigitalio.PiFaceDigital()
        
    @Validate    
    def start(self, context):
        pass
        #self.on()

    @Invalidate    
    def stop(self, context):
        pass
        #self.off()

    def get_name(self):
        return self._name

    def get_state(self):
        return self._state

    def on(self):
        self._state = "on"
        self._pif.relays[0].turn_on()
#        time.sleep(2)
        return "on"

    def off(self):        
        self._state = "off"
        self._pif.relays[0].turn_off()
#        time.sleep(2)
        return "off"

    # Java API compliance
    getName = get_name
    getState = get_state    
