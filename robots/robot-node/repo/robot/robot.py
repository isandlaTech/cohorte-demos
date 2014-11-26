#!/usr/bin/python

from pelix.ipopo.decorators import ComponentFactory, Provides

@ComponentFactory("robot_factory")
@Provides("robot.service")
class Robot(object):

    def __init__(self):
        self._name = "robot"
        self._target = (-1, -1)
        self._position = (0, 0)

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_target(self, x, y):
        self._target = (x, y)

    def get_position(self):
        # update position
        self._position