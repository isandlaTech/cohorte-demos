#!/usr/bin/python

from pelix.ipopo.decorators import ComponentFactory, Provides, Requires

@ComponentFactory("controller_factory")
@Provides("controller.service")
@Requires("_robots", "robot.service", aggregate=True, optional=True)
class Controller(object):

    def __init__(self):
        self._robots = []

    def change_target_position(self, x, y):
        target = {"x": x, "y": y}
        if self._robots:
            for r in self._robots:
                r.set_target(x, y)
        return target

    def get_robots_positions(self):
        robots = {"robots": []}
        if self._robots:
            for r in self._robots:
                position = r.get_position()
                r = {"name": r.get_name(), "x": position[0], "y": position[1]}
                robots["robots"].append(r)
        return robots
