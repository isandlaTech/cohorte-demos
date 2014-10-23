/**
 * Boot configuration for Forkers
 */
{
	/*
	 * Import the common configuration for Python isolates, and the Node
	 * Composer 
	 */
	"import-files" : [ "boot-forker.js" ],

	/*
	 * Components
	 */
	"composition" : [
	/* Configuration of common components */
	{
		"name" : "pelix-http-service",
		"properties" : {
			// Standard forker HTTP port
			"pelix.http.port" : 9000
		}
	}, {
		"name" : "pelix-remote-shell",
		"properties" : {
			// Standard forker remote shell port
			"pelix.shell.port" : 9001
		}
	}
 	]
}
