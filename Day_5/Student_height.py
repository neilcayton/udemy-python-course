student_heights = input("Input a list of student heights ").split()
print(student_heights)
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
h = 0
i =0
for height in student_heights:
    h += height
    i += 1
average = h/i

print(h)
print(i)
print(round(average, 2))