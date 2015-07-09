#!/usr/bin/python

from pelix.ipopo.decorators import ComponentFactory, Provides, Validate, Invalidate, Property
from pelix.ipopo import constants

import time
import pigpio

@ComponentFactory("led_gpio_wrapper_factory")
@Property("_name", "led.name", constants.IPOPO_INSTANCE_NAME)
#@Property("_serial_port", "serial.port", '/dev/tty.usbmodem1d1131')
@Provides("java:/led.services.LedService")
class LedGPIOWrapper(object):

    def __init__(self):
        self._name = "led"
        self._state = "off"
        self.pi = None
        self.wLeds_list = [4,17,27,18,22,23,24,25]
        self._thread = None
        self._terminate = False
        
    @Validate    
    def start(self, context):
        self.pi = pigpio.pi()
        self.wLeds_list = [4,17,27,18,22,23,24,25]
        for wChannel in self.wLeds_list:
            self.pi.set_mode(wChannel, pigpio.OUTPUT)
        if self._thread is None:
            self._thread = threading.Thread(target=self.play)
            self._thread.start()
        self.on()

    @Invalidate    
    def stop(self, context):        
        self.off()
        self._terminate = True
        self._thread = None

    def get_name(self):
        return self._name

    def get_state(self):
        return self._state

    def on(self):        
        self._state = "on"
        

    def off(self):        
        self._state = "off"                      

    def highlight(self, aChannel):
        self.pi.write(aChannel,1)
        time.sleep(0.1)
        self.pi.write(aChannel, 0)
        time.sleep(0.05)

    def highlightSequence(self, aList,aMax):
        for wIdx in range(1,aMax):
            for wChannel in aList:
                self.highlight(wChannel)

    def play(self):
        while self._terminate != True:
            if self._state == "on":              
                wSeqence = [4,17,27,18,22,23,24,25]
                self.highlightSequence(wSeqence,5)
                
                wSeqence = [4,25,17,24,27,23,18,22]
                self.highlightSequence(wSeqence,5)
                
                wSeqence = [25,24,23,22,18,27,17,4]
                self.highlightSequence(wSeqence,5)
            else:
                if self.pi is not None:
                    self.pi.stop()
                time.sleep(1)

        

    # Java API compliance
    getName = get_name
    getState = get_state    