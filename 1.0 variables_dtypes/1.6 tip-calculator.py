print('''
      
      #######              #####                                                                
   #    # #####     #     #   ##   #       ####  #    # #        ##   #####  ####  #####  
   #    # #    #    #        #  #  #      #    # #    # #       #  #    #   #    # #    # 
   #    # #    #    #       #    # #      #      #    # #      #    #   #   #    # #    # 
   #    # #####     #       ###### #      #      #    # #      ######   #   #    # #####  
   #    # #         #     # #    # #      #    # #    # #      #    #   #   #    # #   #  
   #    # #          #####  #    # ######  ####   ####  ###### #    #   #    ####  #    # 
                                                                                          
      
      ''')

# print(''' 
      
#       ''')

# FINAL PROJECT_1.0
# A tip calculator is a simple tool that helps people quickly determine how much to tip at restaurants or for services. It typically takes the bill amount as input and calculates the tip based on a desired percentage (commonly 15%, 18%, or 20%). Some tip calculators also help split the total bill among multiple people.


# STEPS

# STEP 1: Display welcome message to user
print("Welcome to the Tip Calculator!")


# STEP 3: Get input from user
    # 3.1: Get bill amount
bill_amount = float(input("Enter the total bill amount: $"))
    
    # 3.2: Get tip percentage 
tip_percentage = float(input("Enter tip percentage (15, 20, or 30): "))
    
# 3.3: Get number of people 
people=int(input("How many of you are ther\n"))

 # STEP 4: Calculate the tip amount
tip_amount=tip_percentage/100 * bill_amount;

    
 # STEP 5: Calculate total bill including tip
total_bill=tip_amount + bill_amount;


    
    # STEP 6: Calculate amount each person should pay
each_person=total_bill/people
   

    # STEP 7: Display results
    # 7.1: Print header for bill summary    
print("Bill summary___________________");
print(f"the tip amount is {tip_amount}")
print(f"The total bill {total_bill}");
print(f"the amount to e paid by each is {each_person}")

    