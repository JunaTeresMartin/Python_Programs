#AUTHOR   :  JUNA TERES MARTIN
#PROGRAM  :  Program to find the high score from the scores of students using for loop in list
#DATE     :  08-03-2023

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

high_score=student_scores[0]

for s in student_scores:
    if s>high_score:
        high_score=s
print(f"The highest score in the class is: {high_score}")