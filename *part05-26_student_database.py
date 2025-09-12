# soru uzun oldugu icin kopyalamıyorum, websitesine bak istersen

# **CIKARIMLARIM:
# visualizationım zayıf oldugundan uzun data structureları bile comment out edip ara ara bakmalıyım
# add_course() fonksiyonuna tuple pass edildigi halde biz dictionary icinde dictionary yarattık ve tuple immutable oldugundan kullanmadık
# soruyu iyi okumalıyım (3. asamada when adding course information denmiş, when printing degil!)
# ertesi gunde de halen anlamadıgım bir husus varsa llm'e kod yazdırmadan sormalıyım**

def add_student(students:dict, name): #1)adds a student to the database
    students[name] = {}
# eski yanlıs data structure cıkarımım: students["Peter"][0][0]
# students = {'Peter': [('Introduction to Programming', 3), ('Advanced Course in Programming', 2)], 'Eliza': ''}
# yeni ve dogru data structure cıkarımım: students["Peter"]["Introduction to Programming"]
# students = {'Peter': {'Introduction to Programming' : 3, 'Advanced Course in Programming' : 2}}
def print_student(students:dict, name):
    if name not in students:
        print(f"{name}: no such person in the database")
    else:
        if not (students[name]): #dict is empty
            print(name+":\n no completed courses")
        else:
            courses = ""
            total_grade = 0
            course_count = 0
            for course, grade in students[name].items():
                courses += f"  {course} {str(grade)} \n"
                total_grade += grade
                course_count += 1
            print(name+":")
            print("", (course_count), "completed courses:")
            print(courses, end="")
            print(f" average grade {round(total_grade/course_count, 2)}")
            #alt : print(f" average grade {total_grade/course_count:.2f}")
        
def add_course(students:dict, name, course:tuple): #2)adds a course to the student
    lesson = course[0]
    grade = course[1]
    if grade == 0:
        return
    if name in students:
        for course_in_db, grade_in_db in students[name].items():
            if lesson == course_in_db and grade <= grade_in_db:
                return

    students[name][lesson] = grade

def summary(students:dict):
    best_average = 0
    name_with_best_average = ""
    
    most_courses = {}
    name_with_most_courses = ""
    for student, courses in students.items():
        if len(courses) > len(most_courses):
            most_courses = courses
            name_with_most_courses = student
        
        number_of_courses = 0
        total_grades = 0
        for course, grade in courses.items():
            number_of_courses += 1
            total_grades += grade
        
        average = total_grades/number_of_courses
        if average > best_average:
            best_average = average
            name_with_best_average = student

#students = {'Peter': {'Introduction to Programming' : 3, 'Advanced Course in Programming' : 2}}

    print(f"students {len(students)}")
    print(f"most courses completed {len(most_courses)} {name_with_most_courses}")
    print(f"best average grade {best_average} {name_with_best_average}")

if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_course(students, "Peter", ("Algorithms in a Nutshell", 0))
    add_course(students, "Peter", ("Advanced Course in Programming", 0))
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    print_student(students, "Peter")
    
    print()

    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)
