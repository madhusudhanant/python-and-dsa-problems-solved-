#Abstraction in python
#Abstraction is about hiding implementation details and exposing only the essential functionality
from abc import ABC, abstractmethod
class animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    
class dog(animal):
    def sound(self):
        print("dog says bark")
class cat(animal):
    def sound(self):
        print("cat says meow")
d = dog()
c = cat()
d.sound()
c.sound()

Example:
class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    
class car(vehicle):
    def start(self):
        print("car starts with key")
        
class bike(vehicle):
    def start(self):
        print("bike starts with button")
carr = car()
bikee = bike()
carr.start()
bikee.start()
        
