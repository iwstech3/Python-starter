
# creating a dictionary
student={
    "name":"Ngu",
    "age":23,
    "department":"law",
    "gender":"male | female |Other",
    # "favMeal":"ndkf
    
}

# print(student)

# accessing elements inside of a dictionary
name=student["name"]
# print(name)
# Adding items to a dictionary

student["favMeal"]="garri"

# print(student)

# removing items from a dictionary
# del student['name']
# print(student)
# update an item inside of a dictionary
# student["age"]=22
# print(student)

# check the existence of a key in a dictionary
print("name" in student)
# if "name" in student:
# print("character" in student)
# print("age" in student)

#write a loop to print all the items in the dictionary

for keys in student:
    print(keys)
# my_name
# myName

# what if i want keys and values
for  value in student.items():
    print(f"{value}")