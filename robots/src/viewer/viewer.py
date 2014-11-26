#!/usr/bin/python

from pelix.ipopo.decorators import ComponentFactory, Provides, Requires, Property
import pelix.remote
import os
import json


@ComponentFactory("viewer_factory")
@Provides(specifications='pelix.http.servlet')
@Requires("_controller", "controller.service", optional=True)
@Property('_path', 'pelix.http.path', "/robots")
@Property('_reject', pelix.remote.PROP_EXPORT_REJECT, ['pelix.http.servlet'])
class Viewer(object):

    def __init__(self):
        self._controller = None
        self._path = None  

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
        response.send_content(data["meta"]["code"], result, "application/json")

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
        if str(parts[0]) == "robots":
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
                        if str(parts[2]).lower() == "robots":
                            # show robots
                            if self._controller:
                                robots = self._controller.get_robots_positions()
                                self.sendJson(robots, response)
                    elif len(parts) == 4:
                        if str(parts[2]).lower() == "target":
                            target = str(parts[3]).lower()
                            tmp = target.split("-")
                            x = tmp[0]
                            y = tmp[1]
                            if self._controller:
                                # change target position
                                t = self._controller.change_target_position(x, y)
                                self.sendJson(t, response)


