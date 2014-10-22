package spellchecker.checker;

import java.util.*;
import org.apache.felix.ipojo.annotations.*;
import spellchecker.services.*;

@Component(name="spell_checker_factory")
@Provides
public class Checker implements CheckerService {
	Map<String, DictionaryService> dictionaries = 
			new HashMap<String, DictionaryService>();
	
	@Bind(aggregate=true)
	public void bind_dict(DictionaryService dict) {
		this.dictionaries.put(dict.getLanguage(), dict);
	}
	
	@Unbind
	public void unbind_dict(DictionaryService dict) {
		this.dictionaries.remove(dict.getLanguage());
	}
	
	public synchronized List<String> check(String paragraph, String language) {			
		String[] checked_words = paragraph.split(" ");
		DictionaryService dict = this.dictionaries.get(language);
		if (dict != null) {
			List<String> result = new ArrayList<String>();
			for (int i=0; i<checked_words.length; i++) {
				if (dict.check_word(checked_words[i]) == false) {
					result.add(checked_words[i]);
				}
			}
			return result;
		}
		return null;
	}
}
