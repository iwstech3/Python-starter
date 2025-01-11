student_score=input().split("Enter the scores of the students:")
for i in range (0, len(student_score)):
    student_score[i]=int(student_score[i])
highest_score=0;
for i in student_score:
    if i>highest_score:
        highest_score=i
print(highest_score);