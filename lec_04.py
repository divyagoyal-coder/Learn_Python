from enum import Enum
from dataclasses import dataclass
from abc import ABC, abstractmethod

class Colors(Enum):
    RED = 1
    BLUE = 2
    GREEN = 3

# print (Colors.RED.value)




@dataclass
class Animal(ABC):
    '''Abstract Base Class : ABC'''

    name : str

    @abstractmethod
    def speak(self):
        return "Animal Called Speak"

@dataclass
class Dog(Animal):
    # pass
    def speak(self):
        return "Dog Barks"

@dataclass
class Cat(Animal):
    def speak(self):
        pass



dog = Dog("Tony")
print(dog.speak())

cat = Cat("Simpy")
print(cat.speak())