# ACT AS BOARD
# name=input("Enter my name ").lower()

# if name=="gita":
#     print("correct");
# else:
#     print("wrong")

# GITA=WRONG. Gita=wrong, gita

# Exercise: check if a number is odd or even
# num=int(input("enter a number to check")
#         )

# if num%2==0:
#     print("even")
# else:
#     print("odd")


# NESTED IF's

# i need the age and height

height=float(input("Enter your height in m  "));



if height > 1.5:
    # print("You are taken")
    age=int(input("Enter your age "))
    if age < 19:
        gender=input("enter your gender please").lower()
        if gender=="male":
            print("not selected, it turns out, you are male")
        else:
            print("You are selected")
       
    else:
        print("you are over age")
else:
    print("You are out, go home")