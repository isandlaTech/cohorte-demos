{
    "name": "myapp",
    "root": {
        "name": "myapp-composition",
        "components": [
            {
                "factory" : "org.example.temperature.Viewer",
                "name"    : "Viewer",
                "node"    : "node1"
            },
            {
                "factory" : "org.example.temperature.Sensor",
                "name"    : "Sensor",
                "node"    : "node2"
            }
        ]
    }
}