#!/usr/bin/python

from pelix.ipopo.decorators import ComponentFactory, Provides, Validate, Invalidate, Property
from pelix.ipopo import constants

import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 6571
#BUFFER_SIZE = 1024

@ComponentFactory("led_yun_wrapper_factory")
@Property("_name", "led.name", "office-led")
@Provides("java:/led.services.LedService")
class LedYunWrapper(object):

    def __init__(self):
        self._name = "yun_led"
        self._state = "off"
        self._socket = None
        
    @Validate    
    def start(self, context):        
        #self.on()
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect((TCP_IP, TCP_PORT))

    @Invalidate    
    def stop(self, context):        
        #self.off()
        self._socket.close()

    def get_name(self):
        return self._name

    def get_state(self):
        return self._state

    def on(self):             
        self._socket.send("H")
        self._state = "on"
        #data = self._socket.recv(BUFFER_SIZE)

    def off(self):        
        self._socket.send("L")
        self._state = "off"
        #data = self._socket.recv(BUFFER_SIZE)

    # Java API compliance
    getName = get_name
    getState = get_state    