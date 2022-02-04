student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
student_grades = {}
for passing in student_scores:
    score = student_scores[passing]
    if score > 91:
      student_grades[passing] = 'outstanding'
    elif score > 81:
      student_grades[passing] = 'Exceeds Expectations'
    else:
      student_grades[passing] = 'acceptable'


print(student_grades)