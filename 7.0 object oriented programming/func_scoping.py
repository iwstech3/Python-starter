# Function scoping in Python refers to the rules that determine how variables are accessed and modified within functions. Python follows the LEGB rule to resolve variable names, which stands for:

# Local (L) – The innermost scope inside a function, where local variables are defined.
# Enclosing (E) – The scope of outer (enclosing) functions, relevant in nested functions.
# Global (G) – The top-level script or module scope, containing variables defined outside any function.
# Built-in (B) – The outermost scope, containing Python’s built-in functions (like print() or len()).




# 1. Local Scope
# Variables defined inside a function are local to that function and cannot be accessed outside.


# def my_function():
#     x = 10  # Local variable
#     print(x)  # Accessible inside the function

# my_function()
# print(x)  # This would raise a NameError because x is not defined outside the function


# 2. Enclosing Scope (Non-Local Scope)
# If a function is nested inside another function, the inner function can access variables from the outer function.


# def outer():
#     y = 20  # Enclosing variable

#     def inner():
#         print(y)  # Can access y from the enclosing scope

#     inner()

# outer()


# If you want to modify the enclosing variable inside the inner function, use the nonlocal keyword:


# def outer():
#     y = 20

#     def inner():
#         nonlocal y
#         y += 5  # Modifies y in the enclosing scope
#         print(y)

#     inner()
#     print(y)  # Modified value persists

# outer()



# 3. Global Scope
# Variables defined outside functions are in the global scope and can be accessed inside functions, but they cannot be modified directly unless explicitly stated.


# z = 30  # Global variable

# def my_function():
#     print(z)  # Can access z

# my_function()
# To modify a global variable inside a function, use the global keyword:


# z = 30

# def my_function():
#     global z
#     z += 10  # Modifies the global variable
#     print(z)

# my_function()
# print(z)  # The modified value persists