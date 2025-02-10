# Polymorphism in Python

# Polymorphism is one of the core concepts of Object-Oriented Programming (OOP). The term polymorphism means "many forms." In Python, it allows objects of different classes to be treated as objects of a common superclass. This helps in writing flexible and scalable code.

# Types of Polymorphism in Python
# Method Overriding (Runtime Polymorphism)
# Method Overloading (Function Overloading)
# Operator Overloading


# 1. Method Overriding (Runtime Polymorphism)

# Method overriding occurs when a subclass provides a specific implementation of a method that is already defined in its superclass.

# Example: Method Overriding in Inheritance

# class Animal:
#     def speak(self):
#         return "Some sound"

# class Dog(Animal):
#     def speak(self):  # Overriding the parent method
#         return "Bark"

# class Cat(Animal):
#     def speak(self):  # Overriding the parent method
#         return "Meow"

# # Creating objects of subclasses
# dog = Dog()
# cat = Cat()

# print(dog.speak())  # Output: Bark
# print(cat.speak())  # Output: Meow

# This is runtime polymorphism because the method's behavior is determined at runtime.

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Real-World Example: Polymorphism in Action
# Consider a system where different shapes need to be drawn, and each shape has a draw() method.


# class Shape:
#     def draw(self):
#         pass

# class Circle(Shape):
#     def draw(self):
#         print("Drawing a Circle")

# class Rectangle(Shape):
#     def draw(self):
#         print("Drawing a Rectangle")

# class Triangle(Shape):
#     def draw(self):
#         print("Drawing a Triangle")

# # Function demonstrating polymorphism
# def draw_shape(shape):
#     shape.draw()

# # Creating objects of different shapes
# shapes = [Circle(), Rectangle(), Triangle()]

# # Using polymorphism
# for shape in shapes:
#     draw_shape(shape)

# # Output:
# # Drawing a Circle
# # Drawing a Rectangle
# # Drawing a