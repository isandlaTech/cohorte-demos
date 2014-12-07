{
    "name": "robots",
    "root": {
        "name": "robots-composition",
        "components": [
            {
            	"node": "controller-node",
            	"factory": "controller_factory",
            	"name": "Controller"
            }, 
            {
            	"node": "controller-node",
            	"factory": "viewer_factory",
            	"name": "Viewer"
            },
            {
            	"node": "robot1-node",
            	"factory": "robot_factory",
            	"name": "Robot_1"
            },
            {
            	"node": "robot2-node",
            	"factory": "robot_factory",
            	"name": "Robot_2"
            }
        ]
    }
}
