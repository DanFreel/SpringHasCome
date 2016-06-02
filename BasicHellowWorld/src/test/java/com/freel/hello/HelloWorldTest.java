package com.freel.hello;

import org.junit.Assert;
import org.junit.Test;

public class HelloWorldTest 
{
	@Test
	public void testGetMessage()
	{
		Assert.assertEquals("Hello World", new HelloWorld().getMessage());
	}
}
