package spellchecker.services;

public interface DictionaryService {
    boolean check_word(String word);
	String getLanguage();
}
