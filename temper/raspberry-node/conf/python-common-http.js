{
	"import-files" : [ "python-common-http.js" ],

	/*
	 * Components
	 */
	"composition" : [ {
		"name" : "pelix-http-service",
		"properties" : {
			// Use the IPv4 stack on the rapsberry
			"pelix.http.address" : "0.0.0.0"
		}
	} ]
}
