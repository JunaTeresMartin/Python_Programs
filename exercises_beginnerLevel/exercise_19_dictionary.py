#AUTHOR   :  JUNA TERES MARTIN
#PROGRAM  :  Write a program that converts their scores to grades.
#DATE     :  16-03-2023

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades={}
for name in student_scores:
    score=student_scores[name]
    if score>90:
        student_grades[name]="Outstanding"
    elif score>80:
        student_grades[name]="Exceeds Expectations"
    elif score>70:
        student_grades[name]="Acceptable"
    else:
        student_grades[name]="Fail"

print(student_grades)