package spellchecker.services;

import java.util.List;

public interface CheckerService {
	List<String> check(String paragraph, String language);
}
