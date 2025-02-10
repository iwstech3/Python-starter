# Four Pillars of OOP

# The pillars of Object-Oriented Programming (OOP)—Encapsulation, Inheritance, Polymorphism, and Abstraction—are fundamental principles that help in organizing and managing code effectively, especially as projects grow larger and more complex. Each pillar plays a vital role in making the code more modular, reusable, maintainable, and scalable. Here's why each pillar is important:


# Encapsulation (example: a bank account)
# Abstraction (example: a car dashboard)
# Inheritance (example: parent-child traits)
# Polymorphism (example: different modes of payment)

# WHAT IS ENCAPSULATION?

# What It Is: Encapsulation is the concept of bundling the data (attributes) and methods (functions) that operate on the data into a single unit called a class. It also involves restricting access to certain details of an object's implementation.

# Why We Need It:
# Data Hiding: By encapsulating the data, we can hide the internal state of an object from the outside world. This prevents the accidental or unauthorized modification of the object's state.
# Control Over Data: You can expose only the necessary methods to interact with the object's data, keeping implementation details private. This leads to better control over how data is accessed and modified.
# Improved Maintenance: Since implementation details are hidden and can be modified internally without affecting other parts of the system, it makes the code easier to maintain.



# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance  # Private attribute

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount

#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount

#     def get_balance(self):
#         return self.__balance

# account = BankAccount(1000)
# account.deposit(500)
# print(account.get_balance())  # Output: 1500

# # Trying to access the private attribute directly (incorrect way)
# account.__balance = 234  # This will raise an AttributeError\
# print(account.__balance)  # Output: 234

# # Correct way: use getter method
# print(account.get_balance())  # Output: 1500


# WHAT IS NAME MINGLING
# Name mangling in Python refers to the automatic renaming of class attributes that Python performs when you use double underscores (__) at the beginning of a variable name.
# Let me explain with a simple example:
class Dog:
    def __init__(self):
        self.__name = "Rex"  # This gets "mangled"

    def __init__(self):#+
        """#+
        Initialize a Dog object.#+
#+
        This constructor method sets up a new Dog instance with a default name.#+
        The name is stored as a private attribute using name mangling.#+
#+
        Attributes:#+
            __name (str): The name of the dog, set to "Rex" by default.#+
                          This attribute is private and name-mangled.#+
        """#+
        self.__name = "Rex"  # This gets "mangled"
dog = Dog()

# What the name LOOKS like in our code: __name
# What Python ACTUALLY calls it behind the scenes: _Dog__name

# # This is why:
# print(dog.__name)  # Error! Python can't find "__name"
# print(dog._Dog__name)  # Works! Prints "Rex"


# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.__marks = marks  # Private attribute

#     def update_marks(self, new_marks):
#         if 0 <= new_marks <= 100:
#             self.__marks = new_marks

#     def get_marks(self):
#         return self.__marks

# student = Student("Alice", 85)
# student.update_marks(90)
# print(student.get_marks())  # Output: 90



# class User:
#     def __init__(self, username, password):
#         self.username = username
#         self.__password = password  # Private attribute

#     def verify_password(self, input_password):
#         return self.__password == input_password

# user = User("admin", "secure123")
# print(user.verify_password("secure123"))  # Output: True

def check_doc():
    """_summary_
    the function is printing docstring
    """
    print("welcome...")

check_doc()


