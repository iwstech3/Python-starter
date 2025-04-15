# File Systems and File Operations in Python

File systems allow you to store, organize, and retrieve data from a computer. Files can be stored on local storage or remotely, and Python provides easy-to-use methods for interacting with these files. In this guide, we'll explore how to read, write, and manipulate files in Python, along with other important operations.

## 1️⃣ Understanding File Systems

A **file system** organizes and manages files on a storage device (like a hard drive or SSD). It defines the structure and rules for storing and accessing files.

- **File Path**: The location of a file within the file system. It can be absolute or relative.
  - **Absolute Path**: The full path starting from the root directory.
  - **Relative Path**: The path relative to the current directory.

## 2️⃣ Opening Files in Python

To perform operations on files, you must first open the file using the `open()` function. The `open()` function requires the file name and mode as parameters.

### File Modes

- `"r"`: Read (default). Opens the file for reading.
- `"w"`: Write. Opens the file for writing (overwrites if the file exists).
- `"a"`: Append. Opens the file for writing (adds to the end without overwriting).
- `"b"`: Binary mode. Used to read or write binary files.
- `"x"`: Exclusive creation. Creates a new file but fails if the file already exists.

Example of opening a file:

```python
# Open a file for reading
file = open("example.txt", "r")
