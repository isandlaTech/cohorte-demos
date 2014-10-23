{
	"name" : "hello-demo-app-step2",
	"root" : {
		"name" : "hello-demo",
		"components" : [ {
			"name" : "hello_components",
			"factory" : "hello_components_factory",
			"language" : "python",
			"isolate" : "web",			
			"node" : "node1"
		}, {
			"name" : "component_A",
			"factory" : "component_A_factory",
			"language" : "python",
			"isolate" : "components",
			"node" : "node1"
		}, {
			"name" : "component_B",
			"factory" : "component_B_factory",
			"language" : "python",
			"isolate" : "components",
			"node" : "node1"
		}, {
			"name" : "component_C",
			"factory" : "component_C_factory",
			"language" : "python",
			"node" : "node2"
		}  ]
	}
}