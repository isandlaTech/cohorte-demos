#!/usr/bin/python
#-- Content-Encoding: UTF-8 --
"""
Component A.

:author: Bassem Debbabi
:copyright: Copyright 2013, isandlaTech
:license:  Apache Software License 2.0
"""

# iPOPO decorators
from pelix.ipopo.decorators import ComponentFactory, Provides, \
    Validate, Invalidate, Requires, BindField, UnbindField

# Standard library
import logging
import re

@ComponentFactory("component_a_factory")
@Provides("java:/cohorte.demos.hello.HelloService")
class Component_a(object):

    def say_hello(self):
        return "Hi, I am component A!"