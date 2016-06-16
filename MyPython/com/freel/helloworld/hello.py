'''
Created on Jun 15, 2016

@author: Dan
'''

class Hello :
   template_message = "Hello {0}"
   
   def __init__ (self, message) :
      self.message = message
   
   def say_hello (self) :
      print(self.template_message.format(self.message))