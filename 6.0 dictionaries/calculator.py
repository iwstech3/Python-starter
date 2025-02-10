# new concept: how to use dictionaries to solve problems
# how to reuse functions
# difference between print and return

num_1=int(input("Enter the first number"))
operator=input("Enter any operator : ('-', '*', '/', '+')")
num_2=int(input("Enter the second number"))

def add(n1, n2):
    return n1+n2
def  subtract(n1, n2):
    return n1-n2;
def multiply(n1, n2):
    return n1*n2
def divide(n1, n2):
    return n1/n2

operator_box={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

# how do we call the functions

my_function=operator_box[operator]
# operator_box["*"]=>multiply
answer=my_function(num_1, num_2)
print(f"{num_1} {operator} {num_2} = {answer}")