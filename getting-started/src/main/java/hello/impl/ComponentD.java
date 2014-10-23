package hello.impl;

import org.apache.felix.ipojo.annotations.Component;
import org.apache.felix.ipojo.annotations.Provides;

import hello.HelloService;

@Component(name="component_D_factory")
@Provides
public class ComponentD implements HelloService {
	public String say_hello() {
		return "Marhaba, ana composant D ma3moul bi Java!";
	}
}
