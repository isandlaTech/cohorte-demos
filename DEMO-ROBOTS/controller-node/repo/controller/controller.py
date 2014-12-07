#!/usr/bin/python

from pelix.ipopo.decorators import ComponentFactory, Provides, Requires

@ComponentFactory("controller_factory")
@Provides("controller.service")
@Requires("_listeners", "controller.listener", optional=True, aggregate=True)
class Controller(object):

    def __init__(self):
        self._zone_dimensions = {"width": 15, "height": 10}
        self._target_position = {"x": 5, "y": 5}
        self._listeners = []

    def get_zone_dimentions(self):
        return self._zone_dimensions

    def get_target_position(self):
        return self._target_position

    def set_target_position(self, x, y):
        self._target_position["x"] = x
        self._target_position["y"] = y
        for l in self._listeners:
            l.updated_target_position(self._target_position)


