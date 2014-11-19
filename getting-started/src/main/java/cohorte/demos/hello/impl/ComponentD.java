package cohorte.demos.hello.impl;

import org.apache.felix.ipojo.annotations.Component;
import org.apache.felix.ipojo.annotations.Provides;

import cohorte.demos.hello.HelloService;

@Component(name="component_d_factory")
@Provides
public class ComponentD implements HelloService {
	public String say_hello() {
		return "Marhaba, ana composant D ma3moul bi Java!";
	}

	public String get_name() {
		return "D_component";
	}
}

