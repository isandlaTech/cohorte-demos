#!/usr/bin/python3


#
# see "pigpio library"
# http://abyz.co.uk/rpi/pigpio/python.html
#
#

from pelix.ipopo.decorators import ComponentFactory, Provides, Validate, Invalidate, Property
from pelix.ipopo import constants

import collections
import time
import pigpio ## Import  pigpio library
import signal
import sys
import threading
 

@ComponentFactory("led_gpio_wrapper_factory")
@Property("_name", "led.name", constants.IPOPO_INSTANCE_NAME)
#@Property("_serial_port", "serial.port", '/dev/tty.usbmodem1d1131')
@Provides("java:/led.services.LedService")
class LedGPIOWrapper(object):

    def __init__(self):
        self._name = "led"
        self._state = "off"
        self._thread = None
        self._terminate = False

        ## Setup wiringpi 7 = GPIO04 Pin  7 to OUT
        ## Setup wiringpi 0 = GPIO17 Pin 11 to OUT
        ## Setup wiringpi 2 = GPIO27 Pin 13 to OUT
        ## Setup wiringpi 1 = GPIO18 Pin 12 to OUT
        ## Setup wiringpi 3 = GPIO22 Pin 15 to OUT
        ## Setup wiringpi 4 = GPIO23 Pin 16 to OUT
        ## Setup wiringpi 5 = GPIO24 Pin 18 to OUT
        ## Setup wiringpi 6 = GPIO25 Pin 22 to OUT

        self.wLeds_list = [4,17,27,18,22,23,24,25]


        self.kAllLeds = [4,17,27,18,22,23,24,25]

        self.kSeqenceUp = self.kAllLeds
        self.kSeqenceUp2 = [[4],[4,17],[4,17,27],[4,17,27,18],[4,17,27,18,22],[4,17,27,18,22,23],[4,17,27,18,22,23,24],[4,17,27,18,22,23,24,25]]

        self.kSeqenceDown = [25,24,23,22,18,27,17,4]
        self.kSeqenceDown2 = [[25,24,23,22,18,27,17,4],[24,23,22,18,27,17,4],[23,22,18,27,17,4],[22,18,27,17,4],[18,27,17,4],[27,17,4],[17,4],[4]]

        self.kSeqenceAltern = [4,25,17,24,27,23,18,22]
        self.kSeqenceAltern2 = [4,[4,25],[4,25,17],[4,25,17,24],[4,25,17,24,27],[4,25,17,24,27,23],[4,25,17,24,27,23,18],[4,25,17,24,27,23,18,22]]


        self.kNbCycles=3
        self.kTempoAll=0.5
        self.kTempoOne=0.1
        self.kNbExecSequence=5

        self._lightAllOff = True
        self._terminate = False

    @Validate    
    def start(self, context):        
        self.pi = pigpio.pi()
        for wChannel in self.kAllLeds:
            self.pi.set_mode(wChannel, pigpio.OUTPUT)
        self.on()
        

    @Invalidate    
    def stop(self, context):                
        self.off()
        self.lightAllOff()    
        self.pi.stop()
        #self._terminate = True

    def on(self):                
        for led in self.kAllLeds:
            self.lightOnOff(led, True) 
        self._state = "on"
        return "on"                

    def off(self):        
        for led in self.kAllLeds:
            self.lightOnOff(led, False) 
        self._state = "off"          
        return "off"

    def get_name(self):
        return self._name

    def get_state(self):
        return self._state

    #----
    def lightOnOff(self, aChannel,aState):
        self._lightAllOff = False
        wState = 0
        if aState == True:
            wState=1
        if isinstance(aChannel, collections.Iterable):
            for wChannel in aChannel:
                self.pi.write(wChannel,wState)
        else:
            self.pi.write(aChannel,wState)

    #----
    def lightAllOff(self):
        if self._lightAllOff == False:
            self.lightOnOff(self.kAllLeds,False)
            self._lightAllOff = True

    #----
    def highlight(self, aChannel,aDuration=0.1):
        self.lightOnOff(aChannel,True)
        time.sleep(aDuration)
        self.lightOnOff(aChannel,False)
        time.sleep(0.05)

    #----
    def highlightSequence(self, aSequence,aNbExec=5,aDuration=0.1):
        for wIdx in range(1,aNbExec):
            for wChannel in aSequence:
                self.highlight(wChannel,kTempoOne)



