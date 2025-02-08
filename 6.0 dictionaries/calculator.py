# take user input



calculator_done=False

# answer=num_1 + num_2
while not calculator_done:
    num_1=int(input("Enter the first number: "))
    operator=input("Pick an operator from this list ('+','-','*', '/')")
    num_2=int(input("Enter the second number: "))
  
    if operator=="+":
        answer=num_1 + num_2
        print(f"your answer is  {answer}")
    elif operator=="*":
        answer=num_1 *num_2
        print(f"your answer is  {answer}")
        
    elif operator=="-":
        answer=num_1 - num_2
        print(f"your answer is  {answer}")
    elif operator=="/":
        answer=num_1 - num_2
        print(f"your answer is  {answer}")
    else:
        print("Sorry not in there")
    
    
    stop_game=input("type 'y' to continue and 'n' to stop")
    if stop_game=='n':
        calculator_done=True
        
