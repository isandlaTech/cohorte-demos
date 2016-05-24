{
    "name": "led",
    "root": {
        "name": "led-composition",
        "components": [
            {
              	"name" : "led-piface-wrapper",
              	"factory" : "led_piface_wrapper_factory",
              	"node" : "led-uno-piface-raspberry",
              	"isolate" :   "piface",
              	"properties" : {
              		"led.name" : "Lampe_LED"
              	}
            }, {
              	"name" : "led-uno-wrapper",
              	"factory" : "led_uno_wrapper_factory",
              	"node" : "led-uno-piface-raspberry",
              	"isolate" :   "uno",
              	"properties" : {
              		"led.name" : "LED_Arduino_Uno",
              		"serial.port" : "/dev/ttyACM0"
              	}
            }, {
              	"name" : "led-gpio-wrapper",
              	"factory" : "led_gpio_wrapper_factory",
              	"node" : "led-raspberry-gpio",
              	"properties" : {
              		"led.name" : "LED_Raspberry_PI_GPIO"
              	}
            }, {
              	"name" : "led-yun-wrapper",
              	"factory" : "led_yun_wrapper_factory",
              	"node" : "led-arduino-yun",
              	"properties" : {
              		"led.name" : "LED_Arduino_Yun",
              		"serial.port" : "/dev/ttyACM0"
              	}
            }, {
              	"name" : "led-viewer",
              	"factory" : "led_viewer_factory",
              	"isolate" : "web",
              	"node" : "led-gateway"
            }, {
              	"name" : "led-camera-wrapper",
              	"factory" : "led_camera_wrapper_factory",
              	"node" : "led-raspberry-camera",
                "properties" : {
              		"cam.name" : "isandlatech-cam"
              	}
            }
        ]
    }
}
