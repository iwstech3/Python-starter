student_score=input("Enter the scores of the students: ").split()
print(student_score)
# Convert your strings to integers
for i in range (0, len(student_score)):
    student_score[i]=int(student_score[i])
    # we need accumulator
highest_score=0;

for i in student_score:
    if i>highest_score:
        highest_score=i
        print(f"current value of highest score {highest_score}")
print(highest_score);