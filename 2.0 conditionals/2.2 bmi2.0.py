# bmi <18.5-> you are underweight
# bmi greater than 18.5 but below 25, normal weight
# BMI greater than 25 but below 30, slightly overweight
# Bmi over 30, but below 35 obessed
# bmi above 35 you are clinically obesed

# GOOD LUCK

height=float(input("Enter your height in m "));

weight=float(input("Enter your weight in kg "));

bmi=weight/height**2;
# do checks

if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal weight")
elif bmi<30:
    print("slightly overweight")
elif bmi < 35:
    print("obessed")
else:
    print("clinically obessed")    
print(f"Your bmi is {bmi}")