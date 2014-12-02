#!/usr/bin/python

from pelix.ipopo.decorators import ComponentFactory, Provides, Requires, Property
import pelix.remote
import os
import json


@ComponentFactory("led_viewer_factory")
@Provides('pelix.http.servlet')
@Requires("_led", "led.service", optional=True)
@Property('_path', 'pelix.http.path', "/leds")
@Property('_reject', pelix.remote.PROP_EXPORT_REJECT, ['pelix.http.servlet'])
class Viewer(object):

    def __init__(self):
        self._path = None
        self._led = None        

    def get_led(self):
        if self._led:
            return {"state": self._led.get_state()}
        else:
            return {"state": "unknown"}

    def send_action(self, action):
        if self._led:
            if action == "on":
                self._led.on()
            elif action == "off":
                self._led.off()
        return self.get_led()

    """
    Resources -----------------------------------------------------
    """

    def root_dir(self): 
        return os.path.abspath(os.path.dirname(__file__))

    def get_file(self, filename): 
        try:
            src = os.path.join(self.root_dir(), filename)           
            with open(src, 'rb') as fp:
                return fp.read()
        except IOError as exc:
            return str(exc)            

    def load_resource(self, path, request, response):
        mimetypes = {
        ".css": "text/css",
        ".html": "text/html",
        ".js": "application/javascript",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".gif": "image/gif"
        }
        complete_path = os.path.join(self.root_dir(), path)        
        ext = os.path.splitext(path)[1]
        mimetype = mimetypes.get(ext, "text/html")

        content = self.get_file(complete_path)
        return response.send_content(200, content, mimetype)

    def show_main_page(self, request, response):
        content = "<html><head><meta http-equiv='refresh' content='0; URL=" + self._path 
        content += "/static/web/index.html'/></head><body></body></html>"
        response.send_content(200, content)

    def show_error_page(self, request, response):
        content = """<html>
    <head><title>Cohorte Robots</title><head><body><h3>404 This is not the web page you are looking for!</h3></body></html>"""
        response.send_content(404, content)

    def sendJson(self, data, response):
        result = json.dumps(data, sort_keys=False,
                            indent=4, separators=(',', ': '))
        print(result)
        response.send_content(200, result, "application/json")

    """
    Get -----------------------------------------------------------
    """
    def do_GET(self, request, response):
        query = request.get_path()
        # prepare query path: remove first and last '/' if exists
        if query[0] == '/':
            query = query[1:]
        if query[-1] == '/':
            query = query[:-1]
        # get parts of the url
        parts = str(query).split('/')
        if str(parts[0]) == "leds":
            if len(parts) == 1:
                # show main page
                self.show_main_page(request, response)
            elif len(parts) > 1:
                if str(parts[1]) == "static":
                    if len(parts) > 2:
                        self.load_resource('/'.join(parts[2:]), request, response)
                    else:
                        self.show_error_page(request, response)
                elif str(parts[1]) == "api":                    
                    if len(parts) == 3:
                        if str(parts[2]).lower() == "led":
                            t = self.get_led()
                            self.sendJson(t, response)
                    elif len(parts) == 4:
                        if str(parts[2]).lower() == "led":
                            action = str(parts[3]).lower()
                            if action:                                                                
                                t = self.send_action(action)
                                self.sendJson(t, response)


