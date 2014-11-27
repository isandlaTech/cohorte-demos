{
    "name": "robots",
    "root": {
        "name": "robots-composition",
        "components": [
            {
				"name" : "Viewer",
				"factory" : "viewer_factory",
				"node" : "viewer-node"
			}, {
				"name" : "Controller",
				"factory" : "controller_factory",
				"node" : "controller-node"
			}, {
				"name" : "Robot_1",
				"factory" : "robot_factory",
				"node" : "robot1-node"
			}, {
				"name" : "Robot_2",
				"factory" : "robot_factory",
				"node" : "robot2-node"
			}
        ]
    }
}
