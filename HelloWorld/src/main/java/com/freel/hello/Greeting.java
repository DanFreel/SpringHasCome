package com.freel.hello;

public class Greeting
{
   private final Long _id;
   private final String _content;
   
   public Greeting(Long id_, String content_)
   {
      _id = id_;
      _content = content_;
   }

   public Long getId()
   {
      return _id;
   }

   public String getContent()
   {
      return _content;
   }
}
