# CHECK IF A YEAR IS A LEAP YEAR OR NOT
# INSTRUCTIONS
# - On every year that is divisible by 4 without a remainder
#  - Except every year divisible by 100 with no remainder
# Unless the year is also divisible by 400
year=int(input("Enter your year "))

if year%4==0:
    if year%100==0:
        if year%400==0:
            print("A leap year")
        else:
            print("not a leap year")
    else:
        print("A leap year")
else:
    print("Not a leap year")