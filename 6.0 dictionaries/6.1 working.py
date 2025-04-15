
# # creating a dictionary
# # student={
# #     "name":"Ngu",
# #     "age":23,
# #     "department":"law",
# #     "gender":"male | female |Other",
# #     # "favMeal":"ndkf
    
# # }

# # print(student)

# # accessing elements inside of a dictionary
# name=student["name"]
# # print(name)
# # Adding items to a dictionary

# student["favMeal"]="garri"

# # print(student)

# # removing items from a dictionary
# # del student['name']
# # print(student)
# # update an item inside of a dictionary
# # student["age"]=22
# # print(student)

# # check the existence of a key in a dictionary
# print("name" in student)
# # if "name" in student:
# # print("character" in student)
# # print("age" in student)

# #write a loop to print all the items in the dictionary

# for keys in student:
#     print(keys)
#     print(student[keys])
# # my_name
# # myName

# # what if i want keys and values
# for  value in student.items():
#     print(f"{value}")
    
# # for key in student:
   
# # NESTED DICTIONARIES
# # for value in student.values():
# # Person={
# #     "emma":"attributes:{"name":"john", ""}",
# #     "paul":"attributes",
# #     "John":"attributes",
# #     "Mary":"attributes"
# # }
    
    
student={
    "john":{"age":20, "department":"macs", "gender":"male"},
    "peter":{"age":23, "department":"lect", "gender":"male"},
    "mark":{"age":34, "salary":120}
}
print(student["john"]["age"])
# get peters gender
print(student["peter"]["gender"])