package cohorte.demos.hello.impl;

import org.apache.felix.ipojo.annotations.Component;
import org.apache.felix.ipojo.annotations.Provides;

import cohorte.demos.hello.HelloService;

@Component(name="hello_arabic_factory")
@Provides
public class HelloArabic implements HelloService {
	public String say_hello() {
		return "مرحبا، أنا مكون جافا!";
	}

	public String get_name() {
		return "AR";
	}
}

