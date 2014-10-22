package spellchecker.dictionaries;

import java.util.*;
import org.apache.felix.ipojo.annotations.*;
import spellchecker.services.DictionaryService;

@Component(name="spell_dictionary_fr_factory")
@Provides
public class FrenchDictionary implements DictionaryService {
	List<String> dictionary = 
			Arrays.asList("bonjour", "le", "monde", "au", "a", "ipopo", "tutoriel");
	public boolean check_word(String word) {		
		word = word.toLowerCase().trim();
		return this.dictionary.contains(word);
	}
	public String getLanguage() {		
		return "FR";
	}
}
