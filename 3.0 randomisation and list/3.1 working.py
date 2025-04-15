# modularization : The process of breaking down code into smaller, manageable and reusable components
# a module: A python file that can be define functionality ending in .py

# Random module:
# random integer
# random float

import my_own
import random
# generate random numbers between 1 and 10

random_numbers=random.randint(1, 10)
print(random_numbers)
# print(my_own.PI)

# The random method generate numbers between 0 and 0.999999 - not including 1

print(random.random())


# UNDERSTANDING PYTHON LISTS
# name="paul", "johnffd";
names=["Desmond", "Lordsy", "Faith", "Kingsley"];

print(names)
# adding items to the list: method-append()
names.append("Beleh")
print(names)

# Accessing items in a list:
print(f"Desmond:  {names[0]}")
print(f"Desmond:  {names[1]}")

# how many items are inside of the list
my_length=len(names)

print(my_length)
# insert(x, y) x=position or index to insert, y="the item to insert"
another_person=names.insert(1, "Brandon")
# print(another_person)
print(names)

# POPPING- REMOVING FROM A LIST

item_removed=names.pop(0);
item_removed2=names.pop(3);

print(item_removed)
print(item_removed2)

print("After removing item from index 0")
print(names)

# removed method
print("removing lordsy")
sorry_lordsy=names.remove("Lordsy")
print(names)

# SLICING
# a list of numbers

my_numbers=[12, 24, 36, 48, 64]

# [x:y]-> getting elements starting and including x to but not including y
# [1:3]
print("SLICING_______")
print(my_numbers[1:3]);
# [:x]=>printing first item to but not including x
print("Second flavour")
print(my_numbers[:3])
# reverse items in the list
# [::-1]
print("Reverse my lists")
print(my_numbers[::-1])
# EXPLORE THE SLICE METHODS

people=["Faith", "Beleh", "Patrick"];
# choice
person_to_pay=random.choice(people);
print("The person to pay the bill")
print(person_to_pay)
















# UNDERSTANDING LIST, TUPLES AND SETS IN PYTHON

african_countries = [
    ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde"],
    ["Cameroon", "Central African Republic", "Chad", "Comoros", "Democratic Republic of the Congo", "Republic of the Congo", "Djibouti"],
    ["Egypt", "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia", "Gabon", "Gambia"],
    ["Ghana", "Guinea", "Guinea-Bissau", "Ivory Coast", "Kenya", "Lesotho", "Liberia"],
    ["Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco"],
    ["Mozambique", "Namibia", "Niger", "Nigeria", "Rwanda", "Sao Tome and Principe", "Senegal"],
    ["Seychelles", "Sierra Leone", "Somalia", "South Africa", "South Sudan", "Sudan", "Tanzania"],
    ["Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"]
]


# print(african_countries[1:4]);

# slice elements





