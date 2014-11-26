{
    "name": "robots",
    "root": {
        "name": "robots-composition",
        "components": [
            {
				"name" : "Viewer",
				"factory" : "viewer_factory",
				"node" : "controller-node"
			}, {
				"name" : "Controller",
				"factory" : "controller_factory",
				"node" : "controller-node"
			}, {
				"name" : "Robot-1",
				"factory" : "robot_factory",
				"node" : "robot-node"
			}
        ]
    }
}
