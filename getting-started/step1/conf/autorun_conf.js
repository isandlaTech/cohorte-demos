{
	"name" : "hello-demo-app-step1",
	"root" : {
		"name" : "hello-demo",
		"components" : [ {
			"name" : "hello_components",
			"factory" : "hello_components_factory",
			"language" : "python",
			"isolate" : "web"
		}, {
			"name" : "component_A",
			"factory" : "component_A_factory",
			"language" : "python",
			"isolate" : "components"
		}, {
			"name" : "component_B",
			"factory" : "component_B_factory",
			"language" : "python",
			"isolate" : "components"
		}, {
			"name" : "component_C",
			"factory" : "component_C_factory",
			"language" : "python",
			"isolate" : "components"
		}  ]
	}
}