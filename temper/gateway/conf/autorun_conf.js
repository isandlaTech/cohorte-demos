
{
	"name" : "temper-app-v1",
	"root" : {
		"name" : "temper-app-v1-composition",
		"components" : [ 
			{
			/**
			 * Python sensor
			 */
			"name" : "PS",
			"factory" : "python-sensor-factory",
			"isolate" : "temper.python",
			"node" : "python-sensor-pc",
			"properties" : {
				"temper.value.min" : -5,
				"temper.value.max" : 45
			}
		}, {
			/**
			 * Raspberry Pi sensor
			 */
			"name" : "PS-raspi",
			"factory" : "python-sensor-factory",
			"isolate" : "temper.raspi",
			"node" : "raspberry-pi"
		}, {
			/**
			 * Java sensor
			 */
			"name" : "JS",
			"factory" : "java-sensor-factory",
			"isolate" : "temper.java",
			"node" : "java-sensor-pc"
		}, {
			/**
			 * Aggregator component
			 */
			"name" : "A",
			"factory" : "aggregator-factory",
			"language" : "python",
			"isolate" : "aggregation",
			"node" : "gateway",
			"properties" : {
				"poll.delta" : 1
			}
		}, {
			/**
			 * Aggregator web UI
			 */
			"name" : "UI",
			"factory" : "aggregator-ui-factory",
			"language" : "python",
			"isolate" : "web.interface",
			"node" : "gateway",
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

