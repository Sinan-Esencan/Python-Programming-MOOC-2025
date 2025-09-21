# soru 3 aşamadan olustugu ve uzun oldugu icin siteden bak

if True: #*bu conditionı false yapıyoruz testing sırasında*
    # this is not executed during testing
    student_file = input("Student information: ")
    exercise_file = input("Exercises completed: ")
    exam_file = input("Exams completed: ")
else:
    # hard-coded input which is used to gain time during testing
    student_file = "students1.csv"
    exercise_file = "exercises1.csv"
    exam_file = "exam_points1.csv"

students = {}
with open(student_file) as new_file:
    for line in new_file:
        parts = line.strip().split(";")
        if parts[0] == "id":
            continue
        id = parts[0]
        students[id] = f"{parts[1]} {parts[2]}"
    # print(students)

total_no_of_ex = {}
with open(exercise_file) as new_file:
    for line in new_file:
        parts = line.strip().split(";")
        if parts[0] == "id":
            continue
        id = parts[0]
        sum_points = 0
        for point in parts[1:]:
            sum_points += int(point) #int yapmamız onemli
        #*alt:*
        # for i in range(1, 8):
        #     sum_points += int(parts[i])
        total_no_of_ex[id] = sum_points
    # print("total_no_of_ex:", total_no_of_ex)

exam_points = {}
with open(exam_file) as new_file:
    for line in new_file:
        parts = line.strip().split(";")
        if parts[0] == "id":
            continue
        id = parts[0]
        sum_points = 0
        for point in parts[1:]:
            sum_points += int(point) #int yapmamız onemli
        exam_points[id] = sum_points
    # print("exam_points:", exam_points)

def grade_calculator(exercise_points, exam_points):
    total = exercise_points + exam_points
    if total <= 14:
        grade = 0
    elif total <= 17: 
        grade = 1
    elif total <= 20: 
        grade = 2
    elif total <= 23: 
        grade = 3
    elif total <= 27: 
        grade = 4
    else: 
        grade = 5
    return grade
# alt - mooc'den:
# def grade(total_points):
#     a = 0
#     limits = [15, 18, 21, 24, 28]
#     while a < 5 and total_points >= limits[a]:
#         a += 1
#     return a

print(f"{'name':<30}{'exec_nbr':<10}{'exec_pts.':<10}{'exm_pts.':<10}{'tot_pts.':<10}{'grade':<10}")
for id, full_name in students.items():
    if id in total_no_of_ex and id in exam_points:
        exercise_points = int(total_no_of_ex[id]/40*10)
        grade = grade_calculator(exercise_points, exam_points[id])
        total_points = exercise_points + exam_points[id]
        print(f"{full_name:<30}{total_no_of_ex[id]:<10}{exercise_points:<10}{exam_points[id]:<10}{total_points:<10}{grade:<10}")
    else:
        print(name, "has a missing exercise and/or exam")
