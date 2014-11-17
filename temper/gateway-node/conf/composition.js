{
    "name": "temper-demo",
    "root": {
        "name": "temper-demo-composition",
        "components": [
            {
				/**
				 * Python sensor
				 */
				"name" : "PythonSensor",
				"factory" : "python-sensor-factory",
				"isolate" : "temper.python",
				"node" : "python-sensor-node",
				"properties" : {
					"temper.value.min" : -5,
					"temper.value.max" : 45
				}
			}, {
				/**
				 * Raspberry Pi sensor
				 */
				"name" : "PythonSensor-raspi",
				"factory" : "python-sensor-factory",
				"isolate" : "temper.raspi",
				"node" : "raspberry-node"
			}, {
				/**
				 * Java sensor
				 */
				"name" : "JavaSensor",
				"factory" : "java-sensor-factory",
				"isolate" : "temper.java",
				"node" : "java-sensor-node"
			}, {
				/**
				 * Aggregator component
				 */
				"name" : "Aggregator",
				"factory" : "aggregator-factory",
				"language" : "python",
				"isolate" : "aggregation",
				"node" : "gateway-node",
				"properties" : {
					"poll.delta" : 1
				}
			}, {
				/**
				 * Aggregator web UI
				 */
				"name" : "UserInterface",
				"factory" : "aggregator-ui-factory",
				"language" : "python",
				"isolate" : "web.interface",
				"node" : "gateway-node",
				"properties" : {
					"servlet.path" : "/temper"
				},
				"wires" : {
					"_aggregator" : "aggregator"
				}
			}
        ]
    }
}
