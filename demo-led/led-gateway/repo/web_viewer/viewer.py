#!/usr/bin/python

from pelix.ipopo.decorators import ComponentFactory, Provides, Requires, Property, \
             BindField, UnbindField
import pelix.remote
import os
import json
import time
import uuid

import logging
_logger = logging.getLogger("viewer.viewer")

@ComponentFactory("led_viewer_factory")
@Provides('pelix.http.servlet')
@Requires("_leds", "java:/led.services.LedService", optional=True, aggregate=True)
@Requires("_cams", "java:/led.services.CameraService", optional=True, aggregate=True)
@Property('_path', 'pelix.http.path', "/")
@Property('_reject', pelix.remote.PROP_EXPORT_REJECT, ['pelix.http.servlet'])
class Viewer(object):

    def __init__(self):
        self._path = None
        self._leds = []
        self._leds_map = {}
        self._leds_list_lastupdate = time.time()
        self._cams = []
        self._cams_map = {}
        self._uuid = None
        self._time_uuid = 0

    def get_lastupdate(self):
        result = {"lastupdate" : self._leds_list_lastupdate}
        return result

    def get_leds(self):
        #_logger.critical("get_leds")
        result = {"leds": []}
        for led in self._leds_map:
            state = self._leds_map[led]["svc"].get_state()
            result["leds"].append({"name": led, "state": state})
        return result

    def get_led(self, led):
        #_logger.critical("get_led %s", led)
        result = {}
        if led in self._leds_map:
            result["name"] = led
            state = self._leds_map[led]["svc"].get_state()
            result["state"] = state
            return result
        else:
            return {"name": "unknown", "state": "unknown"}

    def get_cams(self):
        #_logger.critical("get_cams")
        result = {"cams": []}
        for cam in self._cams_map:
            state = self._cams_map[cam]["svc"].get_state()
            result["cams"].append({"name": cam, "state": state})
        return result

    def get_cam(self, cam):
        #_logger.critical("get_cam %s", cam)
        result = {}
        if cam in self._cams_map:
            result["name"] = cam
            state = self._cams_map[cam]["svc"].get_state()
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
                result["state"] = self._leds_map[led]["svc"].on()
            elif action == "off":
                result["state"] = self._leds_map[led]["svc"].off()
        return result

    def send_action_cam(self, cam, action):
        _logger.critical("send_action_cam %s to led: %d", action, cam)
        result = {}
        _cam = self._cams_map[cam]
        if _cam:
            result["name"] = cam
            if action == "picture":
                result["state"] = "not busy"
                result["res"] = self._cams_map[cam]["svc"].takePicture()
        _logger.critical("RES : %s", result["res"])
        return result

    @BindField('_leds')
    def on_bind_led(self, field, svc, svc_ref):
        #_logger.critical("binding a new led...")
        props = svc_ref.get_properties()
        led_name = props.get("led.name")
        led_name = str(led_name).lower()
        self._leds_map[led_name] = {}
        self._leds_map[led_name]["svc_ref"] = svc_ref
        self._leds_map[led_name]["svc"] = svc
        self._leds_list_lastupdate = time.time()
        _logger.critical("name: %s", led_name)

    @UnbindField('_leds')
    def on_unbind_led(self, field, svc, svc_ref):
        #_logger.critical("unbinding a led...")
        props = svc_ref.get_properties()
        led_name = props.get("led.name")
        led_name = str(led_name).lower()
        del self._leds_map[led_name]
        self._leds_list_lastupdate = time.time()
        #_logger.critical("name: %s", led_name)

    @BindField('_cams')
    def on_bind_cam(self, field, svc, svc_ref):
        _logger.critical("binding a new cam...")
        props = svc_ref.get_properties()
        cam_name = props.get("cam.name")
        cam_name = str(cam_name).lower()
        self._cams_map[cam_name] = {}
        self._cams_map[cam_name]["svc_ref"] = svc_ref
        self._cams_map[cam_name]["svc"] = svc
        self._leds_list_lastupdate = time.time()
        #_logger.critical("name: %s", led_name)

    @UnbindField('_cams')
    def on_unbind_cam(self, field, svc, svc_ref):
        _logger.critical("unbinding a cam...")
        props = svc_ref.get_properties()
        cam_name = props.get("cam.name")
        cam_name = str(cam_name).lower()
        del self._cams_map[cam_name]
        self._leds_list_lastupdate = time.time()
        #_logger.critical("name: %s", led_name)


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
        ".jpg": "image/jpeg",
        ".png": "image/png",
        ".gif": "image/gif"
        }
        complete_path = os.path.join(self.root_dir(), path)
        ext = os.path.splitext(path)[1]
        mimetype = mimetypes.get(ext, "text/html")

        content = self.get_file(complete_path)
        return response.send_content(200, content, mimetype)

    def show_main_page(self, request, response):
        rel_path = self._path
        while len(rel_path) > 0 and rel_path[0] == '/':
            rel_path = rel_path[1:]

        if not rel_path:
            rel_path = ''

        content = "<html><head><meta http-equiv='refresh' content='0; URL=" #+ self._path
        content += rel_path + "static/web/index.html'/></head><body></body></html>"
        response.send_content(200, content)

    def show_error_page(self, request, response):
        content = """<html>
    <head><title>Cohorte Robots</title><head><body><h3>404 This is not the web page you are looking for!</h3></body></html>"""
        response.send_content(404, content)

    def sendJson(self, data, response):
        result = json.dumps(data, sort_keys=False,
                            indent=4, separators=(',', ': '))
        print(result)
        response.set_header("cache-control", "no-cache")
        response.send_content(200, result, "application/json")

    """
    Get -----------------------------------------------------------
    """
    def do_GET(self, request, response):
        """
        (1) /leds/
        (2) /leds/static
        (3) /leds/api/lastupdate
        (4) /leds/api/leds
        (5) /leds/api/leds/ARDUINO_YUN_LED
        (6) /leds/api/leds/ARDUINO_YUN_LED/on
        (7) /leds/api/leds/ARDUINO_YUN_LED/off
        (8) /leds/api/cams
        (9) /leds/api/cams/CAMERA1
       (10) /leds/api/cams/CAMERA1/picture
        """

        if((time.time() - self._time_uuid) > 3) :
            self._uuid = None

        cookie = request.get_header("Cookie")
        uuid_var = str(uuid.uuid4())
        if(cookie != None) :
            uuid_var = str(cookie.split('=')[1])
            if(uuid_var == self._uuid) :
                self._time_uuid = time.time()
                if((time.time() - self._time_uuid) > 800) :
                    response.set_header("Set-Cookie", "sessionToken="+ uuid_var +"; Max-Age=900; path=/")
        else:
            response.set_header("Set-Cookie", "sessionToken="+ uuid_var +"; Max-Age=900; path=/")

        if(self._uuid == None) :
            self._time_uuid = time.time()
            self._uuid = uuid_var

        query = request.get_path()
        # prepare query path: remove first and last '/' if exists
        while len(query) > 0 and query[0] == '/':
            query = query[1:]
        while len(query) > 0 and query[-1] == '/':
            query = query[:-1]
        # get parts of the url

        if len(query) == 0:
            self.show_main_page(request, response)
        else:
            #parts = str(query).split('?')[0].split('/')
            parts = str(query).split('/')
            if len(parts) == 0:
                # show main page
                self.show_main_page(request, response)
                #self.show_error_page(request, response)
            elif len(parts) > 0:
                if str(parts[0]) == "static":
                    if len(parts) > 1:
                        self.load_resource('/'.join(parts[1:]), request, response)
                    else:
                        self.show_error_page(request, response)

                elif str(parts[0]) == "api":

                    if len(parts) == 2:
                        if str(parts[1]).lower() == "leds":
                            t = self.get_leds()
                            if(self._uuid == uuid_var) :
                                t["prioritaire"]="yes"
                            else:
                                t["prioritaire"]="no"
                            self.sendJson(t, response)
                        elif str(parts[1]).lower() == "lastupdate":
                            t = self.get_lastupdate()
                            if(self._uuid == uuid_var) :
                                t["prioritaire"]="yes"
                            else:
                                t["prioritaire"]="no"
                            self.sendJson(t, response)
                        elif str(parts[1]).lower() == "cams":
                            t = self.get_cams()
                            if(self._uuid == uuid_var) :
                                t["prioritaire"]="yes"
                            else:
                                t["prioritaire"]="no"
                            self.sendJson(t, response)
                    elif len(parts) == 3:
                        if str(parts[1]).lower() == "leds":
                            led = str(parts[2]).lower()
                            t = self.get_led(led)
                            if(self._uuid == uuid_var) :
                                t["prioritaire"]="yes"
                            else:
                                t["prioritaire"]="no"
                            self.sendJson(t, response)
                        elif str(parts[1]).lower() == "cams":
                            cam = str(parts[2]).lower()
                            t = self.get_cam(cam)
                            if(self._uuid == uuid_var) :
                                t["prioritaire"]="yes"
                            else:
                                t["prioritaire"]="no"
                            self.sendJson(t, response)
                        elif str(parts[1]).lower() == "connexion":
                            mdp = str(parts[2])
                            t = {}
                            if(mdp=="isandla$38TECH"):
                                self._uuid = uuid_var
                            if(self._uuid == uuid_var) :
                                t["prioritaire"]="yes"
                            else:
                                t["prioritaire"]="no"
                            self.sendJson(t, response)
                    elif len(parts) == 4:
                        if str(parts[1]).lower() == "leds":
                            led = str(parts[2]).lower()
                            action = str(parts[3]).lower()
                            t = self.send_action(led, action)
                            if(self._uuid == uuid_var) :
                                t["prioritaire"]="yes"
                            else:
                                t["prioritaire"]="no"
                            self.sendJson(t, response)
                        elif str(parts[1]).lower() == "cams":
                            cam = str(parts[2]).lower()
                            action = str(parts[3]).lower()
                            t = self.send_action_cam(cam, action)
                            if(self._uuid == uuid_var) :
                                t["prioritaire"]="yes"
                            else:
                                t["prioritaire"]="no"
                            self.sendJson(t, response)
