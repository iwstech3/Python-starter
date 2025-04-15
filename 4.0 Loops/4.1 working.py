# LOOPS: 

# WHAT ARE LOOPS

# Answer
# Loops in programming are used to execute a block of code repeatedly until a certain condition is met. There are mainly three types of loops:


# WHY WE NEED LOOPS IN PROGRAMMING

# ________Loops are essential in programming for several reasons____:

# _Repetitive Tasks_: Loops help in automating repetitive tasks by executing a block of code multiple times without the need for writing the same code over and over again.

# _Iterating Over Data_: Loops are used to iterate over data structures like arrays, lists, or dictionaries to perform operations on each element.

# _Dynamic Control Flow_: Loops provide a way to dynamically control the flow of a program based on certain conditions.

# 1. Processing Lists/Arrays: Loops are used to iterate over elements in a list or array to perform operations on each element.


# fruit=["apple", "banana", "cherry"]
# for mr_stupid in fruit:
#   print(mr_stupid)
  


#2. Searching for Specific Elements: When you need to search for a specific element in a list.
names=["jene", "marion", "peter"]
for name in names:
  # do this
  if name=="jenet":
    break
    print("found it");
  else:
    print("Searching....")
# if there is jenet in the list

# BREAK AND THE CONTINUE KEYWORD:

# list_numbers=[1,2,3,4,5,6,7,8,9]
# for x in list_numbers:
#   if x==4:
#     continue
#   print(x)
  # Continue you skip a number for eg if x==4 you skip 4, for break , you stop there

  
#3 Summing Numbers: When you need to calculate the sum of a list of numbers.

# WHERE WE NEED LOOPS
# for loop in programming
# while loops in programming
# code exercises

# numbers = [1, 2, 3, 4, 5]
# total = 0
# for x in numbers:
#     total += x
# print(total)

# The range() function in Python is used to generate a sequence of numbers. It can be used in for loops to iterate over a sequence of numbers easily

# for i in range(5):
#     # print numbers in the range 0 to 4 : 5 numbers starting from  0
#     print("Hello")
    
# Specifying Start and End
    # range(start, stop): Generates a sequence of numbers from start up to stop without including stop
for i in range(2, 5):
    print(i)
    
    
# Specifying Step Size: range(start, stop, step): Generates a sequence of numbers from start up to stop with a step size of step


# WHILE LOOPS

# While loops are used to execute a block of code repeatedly as long as a condition is true. The condition is checked before executing the block of code, and the loop continues until the condition becomes false.

#1. Counting from 1 to 5

i = 1
while i <= 5:
    print(i)
    i += 1
    # i=i+1

#2. Sum of Numbers up to a Limit

# limit = 10
# total = 0
# i = 1
# while i <= limit:
#     total += i
#     i += 1
# print("Sum of numbers up to", limit, "is:", total)

# 3. Reversing a string

text = "hello"
reversed_text = ""
index = len(text) - 1
while index >= 0:
    reversed_text += text[index]
    index -= 1
print("Reversed text:", reversed_text)


# 4. Infinite Loops 
# An infinite loop is a loop that continues to run indefinitely because the loop condition never becomes false. This can happen when the loop condition is always true or when there is no condition specified.

# while True:   
#     print("This is an infinite loop") 


# 5.  FACTORIAL OF A NUMBER
# n = 5
# factorial = 1
# i = 1
# while i <= n:
#     factorial *= i
#     i += 1
# print("Factorial of", n, "is:", factorial)