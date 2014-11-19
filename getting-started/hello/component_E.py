#!/usr/bin/python
#-- Content-Encoding: UTF-8 --
"""
Component E.

:author: Bassem Debbabi
:copyright: Copyright 2013, isandlaTech
:license:  Apache Software License 2.0
"""

# iPOPO decorators
from pelix.ipopo.decorators import ComponentFactory, Provides, \
    Validate, Invalidate, Requires, BindField, UnbindField

@ComponentFactory("component_e_factory")
@Provides("java:/cohorte.demos.hello.HelloService")
class Component_e(object):

    def say_hello(self):
        return "Ghost E Component!"

    def get_name(self):
        return "E_component"