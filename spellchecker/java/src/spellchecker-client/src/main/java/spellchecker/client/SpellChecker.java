package spellchecker.client;

import java.io.IOException;
import java.util.List;
import javax.servlet.http.*;
import javax.servlet.ServletException;
import org.apache.felix.ipojo.annotations.*;
import org.osgi.service.http.HttpService;
import spellchecker.services.CheckerService;

@Component(name="spell_client_factory")
public class SpellChecker extends HttpServlet {

	@Requires
	CheckerService checker;
	
	@Requires
	HttpService httpService;
	
	@Bind
	public void bind_http(HttpService http) {
		try {
			httpService.registerServlet("/spellchecker", this, null, null);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	@Unbind
	public void unbind_http(HttpService http) {
		httpService.unregister("/spellchecker");
	}
	
	@Override
	protected void doGet(HttpServletRequest req, HttpServletResponse resp)
			throws ServletException, IOException {
		String result = "";
		String paragraph = req.getParameter("paragraph");
		String language = req.getParameter("language");
		if (paragraph == null || language == null) {
			result = "Fill the language and paragraph inputs!";
		} else {
			List<String> misspelled_words = this.checker.check(paragraph, language.toUpperCase());
			if (misspelled_words == null) {
				result = "Dictionary provider for this language is not installed!";
			} else {
				result += "<b>The misspelled words are:</b> ";
				result += "<span style='color:red;'>";
				for (String word : misspelled_words) {
					result += " " + word;
				}
				result += "</span>";
			}
		}
		String html = "";
		html += "<html><head><title>SpellChecker</title></head><body>";
		html += "<h2>Spellchecker Demo</h2>";
		html += "<hr/>";
		html += "<form action=\"/spellchecker\" method=\"get\" >";
		html += "Language: <input type=\"radio\" name=\"language\" value=\"EN\">EN";
		html += "<input type=\"radio\" name=\"language\" value=\"FR\">FR";
		html += "<input type=\"radio\" name=\"language\" value=\"CN\">CN<br/>";
		html += "Paragraph: <input type=\"text\" name=\"paragraph\" size=\"50\"/><br/>";
		html += "<input type=\"submit\" value=\"Check\"/>";
		html += "</form>";
		html += "<hr/>";
		html += result;
		html += "<hr/>";
		html += "</body></html>";
		
		resp.getWriter().write("Hello World");
	}
	
}
