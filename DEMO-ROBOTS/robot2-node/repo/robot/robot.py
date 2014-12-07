#!/usr/bin/python

import threading
import random
from pelix.ipopo.decorators import ComponentFactory, Provides, Requires, Validate, Property
from pelix.ipopo import constants
import logging

_logger = logging.getLogger(__name__)

@ComponentFactory("robot_factory")
@Provides(["robot.service", "controller.listener"])
@Requires("_controller", "controller.service")
@Property("_name", constants.IPOPO_INSTANCE_NAME)
class Robot(object):

    def __init__(self):
        self._name = ""
        self._zone_dimensions = {"width": -1, "height": -1}
        self._position = {"x": 1, "y": 1}
        self._target_position = {"x": -1, "y": -1}
        self._controller = None

    @Validate
    def validate(self, context):
        self._zone_dimensions = self._controller.get_zone_dimentions()
        self._target_position = self._controller.get_target_position()
        self.move()

    # robot.service interface
    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def get_position(self):
        return self._position

    # received events
    def updated_target_position(self, new_position):
        _logger.critical("updating_target_position... %s %s ", new_position["x"], new_position["y"])
        self._target_position["x"] = new_position["x"]
        self._target_position["y"] = new_position["y"]
        _logger.critical("updated_target_position %s %s ", self._target_position["x"], self._target_position["y"])

    # intern actions
    def move(self):
        _logger.critical("move...")
        threading.Timer(1.0, self.move).start()
        _logger.critical("move... target.x %s", self._target_position["x"])
        x = self._target_position["x"]
        if  int(x) == -1:
            self.random_move()
        else:
            self.move_to_target()


    def random_move(self):
        """
        1 2 3
        8 x 4
        7 6 5
        :return:
        """
        _logger.critical("random_move...")
        x = int(self._position["x"])
        y = int(self._position["y"])
        dest = 0
        if x == 0:
            if y == 0:
                dest = random.choice([4, 5, 6])
            elif y == int(self._zone_dimensions["height"] - 1):
                dest = random.choice([2, 3, 4])
            else:
                dest = random.choice([2, 3, 4, 5, 6])
        elif x == int(self._zone_dimensions["width"] - 1):
            if y == 0:
                dest = random.choice([6, 7, 8])
            elif y == int(self._zone_dimensions["height"] - 1):
                dest = random.choice([1, 2, 8])
            else:
                dest = random.choice([1, 2, 6, 7, 8])
        else:
            dest = random.choice([1, 2, 3, 4, 5, 6, 7, 8])
        if dest in (1, 2, 3):
            self._position["y"] = int(self._position["y"]) - 1
        if dest in (7, 6, 5):
            self._position["y"] = int(self._position["y"]) + 1
        if dest in (1, 8, 7):
            self._position["x"] = int(self._position["x"]) - 1
        if dest in (2, 4, 5):
            self._position["x"] = int(self._position["x"]) + 1

    def move_to_target(self):
        _logger.critical("move_to_target... %s %s ", self._target_position["x"], self._target_position["y"])
        tx = int(self._target_position["x"])
        ty = int(self._target_position["y"])
        zh = int(self._zone_dimensions["height"])
        zw = int(self._zone_dimensions["width"])
        x = int(self._position["x"])
        y = int(self._position["y"])

        if x > tx :
            self._position["x"] =  int(self._position["x"]) - 1
        elif x < tx:
            self._position["x"] = int( self._position["x"]) + 1
        else:
            pass
        if y > ty:
            self._position["y"] =  int(self._position["y"]) - 1
        elif y < ty:
            self._position["y"] =  int(self._position["y"]) + 1
        else:
            pass