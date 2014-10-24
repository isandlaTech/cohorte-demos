#!/usr/bin/python
#-- Content-Encoding: UTF-8 --
"""
Component C.

:author: Bassem Debbabi
:copyright: Copyright 2013, isandlaTech
:license:  Apache Software License 2.0
"""

# iPOPO decorators
from pelix.ipopo.decorators import ComponentFactory, Provides, \
    Validate, Invalidate, Requires, BindField, UnbindField

@ComponentFactory("component_C_factory")
@Provides("cohorte.demos.hello.HelloService")
class ComponentC(object):

    def say_hello(self):
        return "Hola, soy un componente C!"