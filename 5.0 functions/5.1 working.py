# WHAT ARE FUNCTIONS IN PYTHON

# def greet():
#     print("Hello seeds")
#     print("i like eating...")
#     # greed()
# greet()


# CALCULATE
# def bmi_calculator():
#     weight=23.1;
#     height=1.3
#     bmi=weight/height**2
#     print(bmi)
# bmi_calculator()
# input("")

# functions with inputs:
def new_greetings(name):
    print(f"My name is {name}")
    
name=input("what is your name? ")
new_greetings(name)


# write function to take in your name, age, your school, your department, and print a story based on that

def band_name(name, age, school, department):
    print(f"My is {name} I am {age} years old from {school}")

name=input("name:")
age=int(print("age: "))
school=input("school")
department=input("your department: ")
band_name(name, age, school, department)
    






























# A function is a block of code that performs a specific task. It takes an input, performs some operations on the input, and then produces an output. Functions are used to organize code into reusable blocks, making it easier to read, understand, and maintain.
def add(a,b):
    return a+b



# A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. In simpler terms, a prime number is a number that is only divisible by 1 and the number itself. Examples of prime numbers include 2, 3, 5, 7, 11, and so on. Prime numbers play a fundamental role in number theory and have various applications in mathematics and computer science, such as cryptography.
def check_prime(num):
    is_prime=True;
    for i in range(2, num):
        if num%i==0:
            is_prime=False
    if is_prime:
        print("is a prime number")
    else:
        print("Not a prime number")