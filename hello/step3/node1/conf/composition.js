{
	"name": "hello-app",
	"root": {
		"name": "hello-app-composition",
		"components": [
			{
				"name"    : "HC",
				"factory" : "hello_components_factory",
				"isolate" : "web",
				"node"    : "node1"
			}, {
				"name"    : "EN",
				"factory" : "hello_english_factory",
				"isolate" : "components-1",
				"node"    : "node1"
			}, {
				"name"    : "FR",
				"factory" : "hello_french_factory",
				"isolate" : "components-1",
				"node"    : "node1"
			}, {
				"name"    : "ES",
				"factory" : "hello_spanish_factory",
				"isolate" : "components-2",
				"node"    : "node2"
			}, {
				"name"    : "AR",
				"factory" : "hello_arabic_factory",
				"isolate" : "components-3",
				"node"    : "node2"
			}, {
				"name"    : "TEST",
				"factory" : "hello_test_factory",
				"isolate" : "components-4",
				"node"    : "node1"				
			}
		]
	}
}
