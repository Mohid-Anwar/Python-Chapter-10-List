scores = input("Input scores separated by space: ")
marks = [int(x) for x in scores.split()]

max_score = max(marks)

for i in range(len(marks)):
    grade = ''
    if marks[i] >= max_score - 10:
        grade = "A"
    elif marks[i] >= max_score - 20:
        grade = "B"
    elif marks[i] >= max_score - 30:
        grade = "C"
    elif marks[i] >= max_score - 40:
        grade = "D"
    else:
        grade = 'E'
    print(f"Student {i + 1} score is {marks[i]} and Grade is {grade}")
