package com.freel.hello;

public class HelloWorld 
{
	public static void main(String[] args) 
	{
		new HelloWorld().run();
	}
	
	public void run ()
	{
		System.out.println(getMessage());
	}
	
	public String getMessage()
	{
		return "Hello World";
	}
}
