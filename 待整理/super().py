# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        print(f"{self.name} makes a sound.")
        
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        
    def speak(self):
        super().speak()
        print(f"{self.name} barks.")
        
dog = Dog("Buddy")
dog.speak()