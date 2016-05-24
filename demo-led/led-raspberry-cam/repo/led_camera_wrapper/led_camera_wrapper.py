#!/usr/bin/python

from pelix.ipopo.decorators import ComponentFactory, Provides, Validate, Invalidate, Property
from pelix.ipopo import constants

import picamera
import time
import base64
import os
import json

import logging
_logger = logging.getLogger("camera.camera")

@ComponentFactory("led_camera_wrapper_factory")
@Property("_name", "cam.name", constants.IPOPO_INSTANCE_NAME)
@Provides("java:/led.services.CameraService")
class LedCameraWrapper(object):

    def __init__(self):
        self._name = "camera"
        self._state = "not buzy"

    @Validate
    def start(self, context):
        pass

    @Invalidate
    def stop(self, context):
        pass

    def get_name(self):
        return self._name

    def get_state(self):
        return self._state

    def takePicture(self):
        self._state = "buzy"
        with picamera.PiCamera() as camera:
            camera.resolution = (640, 480)
            camera.start_preview()
            # Camera warm-up time
            #time.sleep(3)
            camera.capture('foo.jpg')
        self._state = "not buzy"
        str=""
        with open('foo.jpg', "rb") as imageFile:
            str = base64.b64encode(imageFile.read())
            #_logger.critical("str : %s", str)
        os.remove('foo.jpg')
        base64_string = str.decode('utf-8')
        return base64_string

    # Java API compliance
    getName = get_name
    getState = get_state
