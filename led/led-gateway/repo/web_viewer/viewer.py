#!/usr/bin/python

from pelix.ipopo.decorators import ComponentFactory, Provides, Requires, Property, \
             BindField, UnbindField
import pelix.remote
import os
import json

import logging
_logger = logging.getLogger("viewer.viewer")

@ComponentFactory("led_viewer_factory")
@Provides('pelix.http.servlet')
@Requires("_leds", "java:/led.services.LedService", optional=True, aggregate=True)
@Property('_path', 'pelix.http.path', "/leds")
@Property('_reject', pelix.remote.PROP_EXPORT_REJECT, ['pelix.http.servlet'])
class Viewer(object):

    def __init__(self):
        self._path = None     
        self._leds = []
        self._leds_map = {}

    def get_leds(self):
        _logger.critical("get_leds")
        result = {"leds": []}
        for led in self._leds_map:            
            state = self._leds_map[led]["svc"].get_state()            
            result["leds"].append({"name": led, "state": state})         
        return result

    def get_led(self, led):
        _logger.critical("get_led %s", led)
        result = {}        
        if led in self._leds_map:
            result["name"] = led
            state = self._leds_map[led]["svc"].get_state()
            result["state"] = state
            return result
        else:    
            return {"name": "unknown", "state": "unknown"}

    def send_action(self, led, action):
        _logger.critical("send_action %s to led: %d", action, led)
        result = {}
        _led = self._leds_map[led]
        if _led:
            result["name"] = led
            if action == "on":
                self._leds_map[led]["svc"].on()
                result["state"] = "on"
            elif action == "off":
                self._leds_map[led]["svc"].off()
                result["state"] = "off"
        return result

    @BindField('_leds')
    def on_bind_led(self, field, svc, svc_ref):
        _logger.critical("binding a new led...")
        props = svc_ref.get_properties()        
        led_name = props.get("led.name")
        self._leds_map[led_name] = {}
        self._leds_map[led_name]["svc_ref"] = svc_ref
        self._leds_map[led_name]["svc"] = svc        
        _logger.critical("name: %s", led_name)

    @UnbindField('_leds')
    def on_unbind_led(self, field, svc, svc_ref):
        _logger.critical("unbinding a led...")
        props = svc_ref.get_properties()    
        led_name = props.get("led.name")
        del self._leds_map[led_name]
        _logger.critical("name: %s", led_name)


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
        """
        (1) /leds/
        (2) /leds/static        
        (3) /leds/api/Leds
        (4) /leds/api/leds/ARDUINO_YUN_LED
        (5) /leds/api/leds/ARDUINO_YUN_LED/on
        (5) /leds/api/leds/ARDUINO_YUN_LED/off
        """
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
                #self.show_error_page(request, response)
            elif len(parts) > 1:
                if str(parts[1]) == "static":
                    if len(parts) > 2:
                        self.load_resource('/'.join(parts[2:]), request, response)
                    else:
                        self.show_error_page(request, response)

                elif str(parts[1]) == "api":                    

                    if len(parts) == 3:
                        if str(parts[2]).lower() == "leds":
                            t = self.get_leds()
                            self.sendJson(t, response)
                    elif len(parts) == 4:
                        if str(parts[2]).lower() == "leds":
                            led = str(parts[3]).lower()
                            t = self.get_led(led)
                            self.sendJson(t, response)

                    elif len(parts) == 5:
                        if str(parts[2]).lower() == "leds":
                            led = str(parts[3]).lower()
                            action = str(parts[4]).lower()                                                     
                            t = self.send_action(led, action)
                            self.sendJson(t, response)


