#!/usr/bin/python
#-- Content-Encoding: UTF-8 --
"""
This bundle provide the web interface component of the Hello Component tutorial.

:author: Bassem Debbabi
:copyright: Copyright 2014, isandlaTech
:license:  Apache Software License 2.0
"""

from pelix.ipopo.decorators import ComponentFactory, Provides, Property, \
    Validate, Invalidate, Requires, BindField, UnbindField
from pelix.utilities import to_str
import pelix.remote

import logging

_logger = logging.getLogger(__name__)

# Name the component factory
@ComponentFactory("hello_components_factory")
@Provides(specifications='pelix.http.servlet')
@Property('_path', 'pelix.http.path', "/hello")

@Requires("_components", "java:/cohorte.demos.hello.HelloService", aggregate=True, optional=True)

# Reject the export the servlet specification as remote service
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
                result += "<li>" + c.get_name() + " <a href='/hello/"+c.get_name()+"''>say hello</a></li>"
            result += "</ul>"

        # handle the message
        message = ""
        query = request.get_path()
        if query[0] == '/':
            query = query[1:]
        if query[-1] == '/':
            query = query[:-1]
        parts = str(query).split('/')        
        if len(parts) >= 2:
            comp = self.get_component(parts[1]) 
            if comp:
                message = "<b>" + parts[1] + " says: </b>" + comp.say_hello()
            
        content = """<html>
    <head>
    <title>Hello Components</title>
    </head>
    <body>
    <h2>Hello, Components!</h2>
    <hr/>
    {comps}
    <hr/>
    {msg}
    <hr/>
    </body>
    </html>""".format(comps=result, msg=message)
        response.send_content(200, content)

    def get_component(self, name):
        for c in self._components:
            if c.get_name().lower() == name.lower():
                return c
        return None