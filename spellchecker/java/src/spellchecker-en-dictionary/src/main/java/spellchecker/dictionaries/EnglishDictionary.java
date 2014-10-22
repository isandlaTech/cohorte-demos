package spellchecker.dictionaries;

import java.util.*;
import org.apache.felix.ipojo.annotations.*;
import spellchecker.services.DictionaryService;

@Component(name="spell_dictionary_en_factory")
@Provides
public class EnglishDictionary implements DictionaryService {
	List<String> dictionary = 
			Arrays.asList("hello" , "world", "welcome", "to", "cohorte");
	public boolean check_word(String word) {		
		word = word.toLowerCase().trim();
		return this.dictionary.contains(word);
	}
	public String getLanguage() {		
		return "EN";
	}
}
