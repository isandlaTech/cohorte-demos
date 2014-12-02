{
    "name": "led",
    "root": {
        "name": "led-composition",
        "components": [
            {
							"name" : "led-wrapper",
							"factory" : "led_wrapper_factory",
							"isolate" : "micro-nodes-isolate",
							"node" : "led-gateway"
						}, {
							"name" : "led-viewer",
							"factory" : "led_viewer_factory",		
							"isolate" : "app-isolate",					
							"node" : "led-gateway"
						}
        ]
    }
}
