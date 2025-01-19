bound1=int(input("From: "))
bound2=int(input("To: "))
sum=0
for i in range(bound1, bound2+1):
    if i%2==0:
        print(f"List of even numbers : {i}")
        sum=sum+i
        print(f"sum at this interval is {sum}")
print(f"The final sum is {sum}")

