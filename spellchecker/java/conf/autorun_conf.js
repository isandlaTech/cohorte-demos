{
	"name" : "spellchecker-demo-app",
	"root" : {
		"name" : "spellchecker-java-demo",
		"components" : [ {
			/**
			 * EN Dictionary
			 */
			"name" : "dictionary_en_java",
			"factory" : "spell_dictionary_en_factory",
			"language" : "java"
		}, {
			/**
			 * FR Dictionary
			 */
			"name" : "dictionary_fr_java",
			"factory" : "spell_dictionary_fr_factory",
			"language" : "java"
		}, {
			/**
			 * Spell Checker
			 */
			"name" : "spell_checker_java",
			"factory" : "spell_checker_factory",
			"language" : "java"
		}, {
			/**
			 * Spell Client
			 */
			"name" : "spell_client_java",
			"factory" : "spell_client_factory",
			"language" : "java"
		} ]
	}
}