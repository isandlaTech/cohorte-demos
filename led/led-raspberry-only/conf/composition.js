{
    "name": "raspberry-app",
    "root": {
        "name": "raspberry-app-composition",
        "components": [
            {
				"name" : "led-uno-wrapper",
				"factory" : "led_uno_wrapper_factory",
				"properties" : {
					"led.name" : "my-led",
					"serial.port" : "/dev/ttyACM0"
				},
				"isolate" : "devices" 
			},
			{
				"name" : "led-viewer",
				"factory" : "led_viewer_factory",
				"isolate" : "ui"
			}
        ]
    }
}
