#!/usr/bin/python
#-- Content-Encoding: UTF-8 --
"""
This bundle provide the web interface component of the Hello Component tutorial.

:author: Bassem Debbabi
:copyright: Copyright 2014, isandlaTech
:license:  Apache Software License 2.0
"""

from pelix.ipopo.decorators import ComponentFactory, Provides, Property, \
    Validate, Invalidate, Requires
from pelix.utilities import to_str
import pelix.remote

import logging
# Basic HTTP server


# Name the component factory
@ComponentFactory("hello_components_factory")
@Provides(specifications='pelix.http.servlet')
@Property('_path', 'pelix.http.path', "/hello")
@Requires("_components", "java:/cohorte.demos.hello.HelloService", aggregate=True, optional=True)
# Reject the export the servlet specification
@Property('_reject', pelix.remote.PROP_EXPORT_REJECT, ['pelix.http.servlet'])

class HelloComponents(object):
    def __init__(self):
        self._path = None
        self._components = []

    def do_GET(self, request, response):
        result = ""
        if not self._components:
            result = "No components! :/"
        else:
            result += "<ul>"
            for c in self._components:
                result += "<li>" + c.say_hello() + "</li>"
            result += "</ul>"
        content = """<html>
    <head>
    <title>Hello Components</title>
    </head>
    <body>
    <h2>Hello, Components!</h2>
    <hr/>
    {result}
    <hr/>
    </body>
    </html>""".format(result=result)
        response.send_content(200, content)
