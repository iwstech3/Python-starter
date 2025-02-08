# 1️⃣ Writing to a File
# To write data to a file, you need to open it in write ("w") or append ("a") mode.

# THE with keyword in python:  In Python, the with keyword is used for context management. It ensures that resources are properly acquired and released when they are no longer needed, avoiding potential issues like resource leaks. The with statement is used to wrap the execution of a block of code within methods defined by the context manager. This allows common preparation and cleanup tasks to be performed automatically.


# Without with (Using try-finally)


file = open("file.txt", "r")
try:
    content = file.read()
    print(content)
finally:
    file.close()  # Must manually close the file




# Using with Statement:
# It's a good practice to use the with statement when opening a file to ensure it is automatically closed after operations are complete.


with open("example.txt", "r") as file:
    content = file.read()
    print(content)\
        


# 3️⃣ Reading Files
# Read the Entire File
# To read the entire file content as a string:


with open("example.txt", "r") as file:
    content = file.read()  # Reads the entire file
    print(content)        
    
    
# Read Line by Line
# To read the file line by line:


with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())  # Remove trailing newline characters
        


# Read Specific Number of Characters
# To read a specific number of characters:


with open("example.txt", "r") as file:
    content = file.read(10)  # Reads the first 10 characters
    print(content)


# Read as List of Lines
# To read the file as a list of lines:


with open("example.txt", "r") as file:
    lines = file.readlines()  # Returns a list of lines
    print(lines)
    
# 4️⃣ Writing Files
# To write data to a file, use the "w", "a", or "x" modes.


with open("example.txt", "w") as file:
    file.write("This is a new line of text.\n")
    
# Append to a File

with open("example.txt", "a") as file:
    file.write("This is an appended line.\n")


# Writing Multiple Lines

lines = ["First line\n", "Second line\n", "Third line\n"]
with open("example.txt", "w") as file:
    file.writelines(lines)  # Writes a list of lines
    
# 5️⃣ Handling File Not Found Errors
# When you attempt to open a file that does not exist, a FileNotFoundError will occur. You can handle it using try-except blocks:


try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found! Please check the file path.")



# 6️⃣ Working with Binary Files
# Binary files store data in a format that isn't human-readable (e.g., images, audio files). To handle binary files, open them in binary mode.

# Reading Binary Files


with open("image.jpg", "rb") as file:
    content = file.read()  # Reads the binary content


with open("copy_image.jpg", "wb") as file:
    file.write(content)  # Writes the binary content to a new file