# **Exception Handling in Python**

## **1. What is Exception Handling?**
Exception handling in Python is a mechanism to handle errors **gracefully** without crashing the program. Python provides the `try-except` block to catch and manage exceptions.

## **2. Why Use Exception Handling?**
- Prevents program crashes due to unexpected errors.
- Helps in debugging by providing error messages.
- Ensures proper resource cleanup (like closing files or database connections).
- Improves user experience by handling errors smoothly.

---

## **Basic Exception Handling: `try-except`**
The `try` block contains the code that might cause an exception, and the `except` block handles the exception.

### **Example: Handling Division by Zero**
```python
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
```

### **Output**
```
Error: Cannot divide by zero!
```
🔹 Without exception handling, this would crash the program.

---

## **3. Catching Multiple Exceptions**
You can handle different types of exceptions separately.

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Invalid input! Please enter a number.")
```

### **Output**
```
Enter a number: abc
Error: Invalid input! Please enter a number.
```

---

## **4. Using `except Exception` to Catch All Errors**
You can catch **any type of exception** using `except Exception` (not recommended unless necessary).

```python
try:
    result = 10 / int("abc")
except Exception as e:
    print(f"An error occurred: {e}")
```

### **Output**
```
An error occurred: invalid literal for int() with base 10: 'abc'
```
🔹 **Note:** It's better to catch specific exceptions when possible.

---

## **5. Using `else` with `try-except`**
The `else` block runs only if **no exception occurs**.

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
else:
    print(f"Result: {result}")  # Runs only if no exception occurs
```

---

## **6. Using `finally` for Cleanup**
The `finally` block **always executes** (even if an exception occurs). It's useful for **resource cleanup** (closing files, database connections, etc.).

```python
try:
    file = open("example.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Error: File not found!")
finally:
    file.close()  # Ensures the file is closed
```

---

## **7. Raising Custom Exceptions (`raise`)**
You can manually raise exceptions using `raise`.

```python
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or above")
    return "Access granted!"

try:
    print(check_age(16))
except ValueError as e:
    print(f"Error: {e}")
```

### **Output**
```
Error: Age must be 18 or above
```

---

## **8. Creating Custom Exception Classes**
You can define your own exception classes by inheriting from `Exception`.

```python
class CustomError(Exception):
    """Custom exception class"""
    pass

try:
    raise CustomError("This is a custom exception!")
except CustomError as e:
    print(f"Caught: {e}")
```

---

## **9. When to Use Exception Handling?**
| **Scenario** | **Use Exception Handling?** |
|-------------|----------------------------|
| Handling user input errors (e.g., invalid number input) | ✅ Yes |
| Handling file operations (e.g., missing files) | ✅ Yes |
| Handling API/network requests (e.g., timeout errors) | ✅ Yes |
| Validating function arguments | ✅ Yes (Use `raise`) |
| Debugging code during development | ❌ No (Use print statements or logging) |

---

## **10. Best Practices for Exception Handling**
✅ **Catch only specific exceptions** (avoid `except Exception` unless necessary).  
✅ **Use `finally` for cleanup** (e.g., closing files or releasing resources).  
✅ **Use `raise` for validation errors** inside functions.  
✅ **Log exceptions** instead of just printing them (`import logging`).  
✅ **Don’t suppress exceptions silently** (provide meaningful error messages).  

---

### **Example: Best Practice Implementation**
```python
import logging

logging.basicConfig(level=logging.ERROR)

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        logging.error(f"Cannot divide by zero: {e}")
        return None  # Returning None instead of crashing

print(safe_divide(10, 0))
```

---

### **Conclusion**
Exception handling is **crucial** for building robust Python programs. It **prevents crashes**, **improves debugging**, and **ensures smooth execution**. Use it wisely for handling expected errors while avoiding overuse.

Would you like real-world use cases or code examples related to your projects? 🚀
# **Exception Handling in Python**

## **1. What is Exception Handling?**
Exception handling in Python is a mechanism to handle errors **gracefully** without crashing the program. Python provides the `try-except` block to catch and manage exceptions.

## **2. Why Use Exception Handling?**
- Prevents program crashes due to unexpected errors.
- Helps in debugging by providing error messages.
- Ensures proper resource cleanup (like closing files or database connections).
- Improves user experience by handling errors smoothly.

---

## **Basic Exception Handling: `try-except`**
The `try` block contains the code that might cause an exception, and the `except` block handles the exception.

### **Example: Handling Division by Zero**
```python
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
```

### **Output**
```
Error: Cannot divide by zero!
```
🔹 Without exception handling, this would crash the program.

---

## **3. Catching Multiple Exceptions**
You can handle different types of exceptions separately.

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Invalid input! Please enter a number.")
```

### **Output**
```
Enter a number: abc
Error: Invalid input! Please enter a number.
```

---

## **4. Using `except Exception` to Catch All Errors**
You can catch **any type of exception** using `except Exception` (not recommended unless necessary).

```python
try:
    result = 10 / int("abc")
except Exception as e:
    print(f"An error occurred: {e}")
```

### **Output**
```
An error occurred: invalid literal for int() with base 10: 'abc'
```
🔹 **Note:** It's better to catch specific exceptions when possible.

---

## **5. Using `else` with `try-except`**
The `else` block runs only if **no exception occurs**.

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
else:
    print(f"Result: {result}")  # Runs only if no exception occurs
```

---

## **6. Using `finally` for Cleanup**
The `finally` block **always executes** (even if an exception occurs). It's useful for **resource cleanup** (closing files, database connections, etc.).

```python
try:
    file = open("example.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Error: File not found!")
finally:
    file.close()  # Ensures the file is closed
```

---

## **7. Raising Custom Exceptions (`raise`)**
You can manually raise exceptions using `raise`.

```python
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or above")
    return "Access granted!"

try:
    print(check_age(16))
except ValueError as e:
    print(f"Error: {e}")
```

### **Output**
```
Error: Age must be 18 or above
```

---

## **8. Creating Custom Exception Classes**
You can define your own exception classes by inheriting from `Exception`.

```python
class CustomError(Exception):
    """Custom exception class"""
    pass

try:
    raise CustomError("This is a custom exception!")
except CustomError as e:
    print(f"Caught: {e}")
```

---

## **9. When to Use Exception Handling?**
| **Scenario** | **Use Exception Handling?** |
|-------------|----------------------------|
| Handling user input errors (e.g., invalid number input) | ✅ Yes |
| Handling file operations (e.g., missing files) | ✅ Yes |
| Handling API/network requests (e.g., timeout errors) | ✅ Yes |
| Validating function arguments | ✅ Yes (Use `raise`) |
| Debugging code during development | ❌ No (Use print statements or logging) |

---

## **10. Best Practices for Exception Handling**
✅ **Catch only specific exceptions** (avoid `except Exception` unless necessary).  
✅ **Use `finally` for cleanup** (e.g., closing files or releasing resources).  
✅ **Use `raise` for validation errors** inside functions.  
✅ **Log exceptions** instead of just printing them (`import logging`).  
✅ **Don’t suppress exceptions silently** (provide meaningful error messages).  

---

### **Example: Best Practice Implementation**
```python
import logging

logging.basicConfig(level=logging.ERROR)

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        logging.error(f"Cannot divide by zero: {e}")
        return None  # Returning None instead of crashing

print(safe_divide(10, 0))
```

---

### **Conclusion**
Exception handling is **crucial** for building robust Python programs. It **prevents crashes**, **improves debugging**, and **ensures smooth execution**. Use it wisely for handling expected errors while avoiding overuse.

Would you like real-world use cases or code examples related to your projects? 🚀
