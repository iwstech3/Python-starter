range_start=int(input("You want to start from: "))

rang_end=int(input("You want to end at: "));


# RUNNING OUR FOR LOOP HERE:
for i in range(range_start, rang_end+1):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)