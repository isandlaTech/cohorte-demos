#!/usr/bin/python
#-- Content-Encoding: UTF-8 --
"""
Component B.

:author: Bassem Debbabi
:copyright: Copyright 2013, isandlaTech
:license:  Apache Software License 2.0
"""

# iPOPO decorators
from pelix.ipopo.decorators import ComponentFactory, Provides, \
    Validate, Invalidate, Requires, BindField, UnbindField

@ComponentFactory("component_B_factory")
@Provides("cohorte.demos.HelloService")
class ComponentB(object):

    def say_hello(self):
        return "Bonjour, je suis un composant B!"