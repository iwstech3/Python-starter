# # definition
# # function calling


# def great_user(name, occupation):
#     print(f"Hello {name} your occupation is {occupation}") 
#     print("hello, user") 
  
    


# my_name=input("what is your name? ")
# my_occupation=input("What is your occupation? ")

# great_user(my_name, my_occupation)
# abcdefghi


# functions with input

# FUNCTIONS WITH OUTPUT

def say_name(name1, name2):
    name_one=name1.title()
    name_two=name2.title()
    
    return f"{name_one} {name_two}"

    
    # return

    
names1=input("Enter your first name")
names2=input("Enter your second  name")
# AM PASSING THIS NOW AS ARGUMENTS
result= say_name(names1, names2)
print(result)

def stop_running():
    sum=0
    for i in range(1, 6):
        if i==3:
            return
        print(f"the value of {i}")
        sum+=i;
    return sum

result=stop_running()
print(result)   
      