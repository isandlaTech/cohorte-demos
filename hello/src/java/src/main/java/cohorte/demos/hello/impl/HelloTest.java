package cohorte.demos.hello.impl;

import org.apache.felix.ipojo.annotations.Component;
import org.apache.felix.ipojo.annotations.Requires;
import org.apache.felix.ipojo.annotations.Instantiate;
import org.apache.felix.ipojo.annotations.Validate;

import cohorte.demos.hello.HelloService;

@Component(name="hello_test_factory")
public class HelloTest {
	
	@Requires(filter="(instance.name=AR)")
	HelloService hello;
	
	@Validate
	public void start() {
		
	}
}

