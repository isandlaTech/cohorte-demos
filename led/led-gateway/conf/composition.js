{
    "name": "led",
    "root": {
        "name": "led-composition",
        "components": [
            {
		"name" : "led--uno-wrapper",
		"factory" : "led_uno_wrapper_factory",
		"node" : "led-raspberry",
		"properties" : {
			"led.name" : "conference-led",
			"serial.port" : "/dev/ttyACM0"
		}
	}, {
		"name" : "led-yun-wrapper",
		"factory" : "led_yun_wrapper_factory",
		"node" : "led-arduino-yun",
		"properties" : {
			"led.name" : "office-led"
		}
	}, {
		"name" : "led-viewer",
		"factory" : "led_viewer_factory",
		"isolate" : "web",
		"node" : "led-gateway"
	}, {
		"name" : "java-swing-ui",
		"factory" : "java_swing_ui_factory",
		"node" : "led-desktop"
	}
        ]
    }
}
