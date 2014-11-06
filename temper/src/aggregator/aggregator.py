#!/usr/bin/env python
# -- Content-Encoding: UTF-8 --
"""
An aggregator of sensors values

Created on 10 juil. 2012

:author: Thomas Calmant
"""

# ------------------------------------------------------------------------------

from pelix.ipopo import constants

from pelix.ipopo.decorators import ComponentFactory, Provides, \
    Validate, Invalidate, Property, Requires, Bind, Unbind

# ------------------------------------------------------------------------------

import logging
import threading
import time

# ------------------------------------------------------------------------------

# Name of the HistoryEntry class in Java, for Jabsorb
HISTORY_ENTRY_CLASS = "temper.aggregator.HistoryEntry"

_logger = logging.getLogger(__name__)

# ------------------------------------------------------------------------------

@ComponentFactory("aggregator-factory")
@Property("_name", constants.IPOPO_INSTANCE_NAME)
@Property("_history_size", "history.size", 10)
@Property("_poll_delta", "poll.delta", 10)
@Requires("_sensors", "java:/temper.sensors.TemperatureService",
          aggregate=True, optional=True)
@Requires("_listeners", "java:/temper.sensors.AggregatorListener",
          aggregate=True, optional=True)
@Provides("java:/temper.aggregator.AggregatorService")
class Aggregator(object):
    """
    Temperature sensor
    """
    def __init__(self):
        """
        Constructor
        """
        self._history_size = 0
        self._name = ""
        self._poll_delta = 0
        self._sensors = []
        self._listeners = []

        # The values history (sensor -> list of dictionaries)
        self._history = {}

        self._lock = threading.Lock()
        self._thread_stop = threading.Event()
        self._thread = None


    def get_history(self):
        """
        Retrieves the whole known history as a dictionary.
        
        Result is a dictionary, with sensor name as entry and a list
        of HistoryEntry (Python map/Java bean) as value
        
        :return: The whole history
        """
        with self._lock:
            return self._history


    def get_sensor_history(self, sensor):
        """
        Retrieves the known history for the given sensor
        
        :param sensor: The name of a sensor
        :return: The history of the sensor. Can be None
        """
        with self._lock:
            return self._history.get(sensor, None)


    def get_sensors(self):
        """
        Retrieves the list of sensors visible in the history
        
        :return: The list of known sensors
        """
        with self._lock:
            return tuple(self._history.keys())

    def get_active_sensors(self):
        """
        Retrieves the active sensors

        :return: The list of active sensors
        """
        sensors = []
        if self._sensors is not None:
            for sensor in self._sensors:
                try:
                    name = sensor.getName()
                    sensors.append(name)
                except Exception as ex:
                    _logger.error("Error retrieving sensor data: %s", ex)

    def _poll(self):
        """
        Polls the value of all known sensors
        """
        while not self._thread_stop.is_set():
            if self._sensors is not None:
                for sensor in self._sensors:
                    try:
                        name = sensor.getName()
                        value = sensor.getValue()
                        unit = sensor.getUnit()
                        self._store(name, value, unit)

                    except Exception as ex:
                        _logger.error("Error retrieving sensor data: %s", ex)

            # Wait for the poll delta, or for the order to stop
            try:
                wait = float(self._poll_delta)

            except:
                wait = 30

            self._thread_stop.wait(wait)


    def _store(self, sensor, value, unit):
        """
        Stores a value in the history
        """
        # Get the history list for this sensor
        with self._lock:
            sensor_history = self._history.setdefault(sensor, [])

            # Remove the oldest entry if needed
            if len(sensor_history) >= self._history_size:
                del sensor_history[-1]

            # Insert the new entry in front
            sensor_history.insert(0, {"sensor": sensor,
                                      "time": int(time.time() * 1000),
                                      "value": value,
                                      "unit": unit,
                                      "javaClass": HISTORY_ENTRY_CLASS})

    def _fire_new_sensor(name, location):
        """
        Informes Aggregator Listeners about the new available Temperature sensor
        """
        for listener in self._listeners:
            listener.newSensor(name, location)


    def _fire_retired_sensor(name, location):
        """
        Informes Aggregator Listeners about the gone Temperature sensor
        """
        for listener in self._listeners:
            listener.retiredSensor(name, location)

    @BindField("_sensors")
    def bindSensor(self, field, svc, ref):
        name = svc.getName()
        location = ref.get_property("location")
        _fire_new_sensor(name, location)

    @UnbindField("_sensors")
    def bindSensor(self, field, svc, ref):
        name = svc.getName()
        location = ref.get_property("location")
        _fire_retired_sensor(name, location)    

    @Bind
    def bind(self, svc, ref):
        """
        Called by iPOPO when a service is bound
        """
        props = ref.get_properties()
        if props.get("service.imported", False):
            import_str = "from %s" % props.get("service.imported.from")
        else:
            import_str = "local"
        # if service is TemperatorSensor then informe listeners        
        _logger.debug("%s> Bound to %s (%s)", self._name, ref, import_str)


    @Unbind
    def unbind(self, svc, ref):
        """
        Called by iPOPO when a service is gone
        """
        props = ref.get_properties()
        if props.get("service.imported", False):
            import_str = "from %s" % props.get("service.imported.from")
        else:
            import_str = "local"
        _logger.debug("%s> UnBound of %s (%s)", self._name, ref, import_str)


    @Validate
    def validate(self, context):
        """
        Component validation
        """
        # Clear the stop event
        self._thread_stop.clear()

        # Start the polling thread
        self._thread = threading.Thread(target=self._poll)
        self._thread.start()
        _logger.info("Component %s validated", self._name)


    @Invalidate
    def invalidate(self, context):
        """
        Component invalidation
        """
        # Set the stop event
        self._thread_stop.set()

        # Wait a little for the thread
        self._thread.join(2)
        self._thread = None

        _logger.info("Component %s invalidated", self._name)


    # Java API compliance
    getHistory = get_history
    getSensorHistory = get_sensor_history
    getSensors = get_sensors
    getActiveSensors = get_active_sensors

