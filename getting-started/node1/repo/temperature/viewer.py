from pelix.ipopo.decorators import ComponentFactory, Provides, Requires, Property
import pelix.remote

@ComponentFactory("org.example.temperature.Viewer")
@Provides('pelix.http.servlet')
@Property('path', 'pelix.http.path', "/")
@Property('reject', pelix.remote.PROP_EXPORT_REJECT, ['pelix.http.servlet'])
@Requires("sensor","TemperatureService")
class Viewer(object):
    def __init__(self):
        sensor = None
        path = None
		
    def do_GET(self, request, response):
        temp = self.sensor.get_temperature()
        result = "<H3>Actual Temperature : {0}</h3>".format(temp)
        response.send_content(200, result, "text/html")