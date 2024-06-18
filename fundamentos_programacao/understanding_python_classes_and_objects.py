# Defining and Instantiating a Class
class Animal:
    def __init__(self, name: str, sound: str) -> None:
        self.name: str = name
        self.sound: str = sound
    
    def make_sound(self):
        return f"{self.name} says {self.sound}"
    
# Creating an instance of Animal
dog = Animal(name="Dog", sound="Woof")
print(dog.make_sound())

# Inherance
class Bird(Animal):
    def __init__(self, name, sound, can_fly) -> None:
        super().__init__(name, sound)
        self.can_fly = can_fly

    def fly(self):
        return "flies" if self.can_fly else "can not fly"
    
# Creating an instance of Bird
sparrow = Bird("Sparrow", "Tweet", True)
print(f"{sparrow.make_sound()} and {sparrow.fly()}")

# Class Method and Static Method
class Rectangle:
    def __init__(self, w, h) -> None:
        self.h = h
        self.w = w

    def area(self):
        return self.h * self.w
    
    @classmethod
    def square(cls, side_length):
        return cls(side_length, side_length)
    
    @staticmethod
    def is_square(w, h):
        return w == h
    
# Criando um retângulo
rectangle = Rectangle(10, 5)
print(rectangle.area())

# Criando um quadrado usando o método de classe
square = Rectangle.square(10)
print(square.area())

# Verificando se um retângulo é um quadrado usando o método estático
print(Rectangle.is_square(rectangle.h, rectangle.w))
print(Rectangle.is_square(square.w, square.h))
