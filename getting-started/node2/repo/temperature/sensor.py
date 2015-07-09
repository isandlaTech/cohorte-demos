from pelix.ipopo.decorators import ComponentFactory, Provides 
from random import randrange

@ComponentFactory("org.example.temperature.Sensor")
@Provides("TemperatureService")
class Sensor(object):
		
    def get_temperature(self):
        return randrange(0, 50)