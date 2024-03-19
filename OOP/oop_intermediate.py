# Encapsulation: We encapsulate the attributes of each class and provide methods to access and modify them.

class Animal:
    def __init__(self, name):
        self._name = name  # Encapsulated attribute

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

# Inheritance: We create subclasses that inherit attributes and methods from a parent class.

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Polymorphism: We define methods in the subclasses with the same name as the method in the parent class, 
#but with different implementations.

def animal_sound(animal):
    return animal.make_sound()

# Usage

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.get_name())  # Accessing encapsulated attribute
print(cat.get_name())

dog.set_name("Max")  # Modifying encapsulated attribute
print(dog.get_name())

print(animal_sound(dog))  # Polymorphism
print(animal_sound(cat))
