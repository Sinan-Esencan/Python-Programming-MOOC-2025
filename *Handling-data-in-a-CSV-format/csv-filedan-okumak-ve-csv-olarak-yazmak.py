# Let's write a program which assesses students' performance on a course. The program reads a CSV file, which contains weekly exercise points received by the students.
# The program then calculates the points total and determines the grade attained by each student. Finally, the program creates a CSV file containing the points total and
# grade for each student.

# The program logic is divided into three functions: reading the file and processing the contents into an accessible format, determining the grade, and writing the file.

# With 1st function the file is read following the principles covered in the previous section. The data is stored in a dictionary, where the key is the student's name,
# and the value is a list of the points received by the student, in integer format. The 2nd function is for determining the grade based on the points received. This 
# function is in turn used by the 3rd function, which writes the results to the file.

def read_weekly_points(filename):
    weekly_points = {}
    with open(filename) as my_file:
        for line in my_file:
            parts = line.split(";") #line.strip().split(";") demek daha iyi pratik
            point_list = []
            for points in parts[1:]:
                point_list.append(int(points))
            weekly_points[parts[0]] = point_list
    # print(weekly_points)
    return weekly_points

def grade(points):
    if points < 20:
        return 0
    elif points < 25:
        return 1
    elif points < 30:
        return 2
    elif points < 35:
        return 3
    elif points < 40:
        return 4
    else:
        return 5

def save_results(filename, weekly_points):
    with open(filename, "w") as my_file:
        for name, point_list in weekly_points.items():
            point_sum = sum(point_list)
            my_file.write(f"{name};{point_sum};{grade(point_sum)}\n")

if __name__ == "__main__":
    weekly_points = read_weekly_points("weekly_points.csv")
    save_results("results.csv", weekly_points)


# Notice how each function defined above is relatively simple, and they all have a single responsibility. This is a common and advisable approach when programming larger wholes.
# The single reponsibility principle makes verifying functionality easier. It also makes it easier to make changes to the program later, and to add new features.
# Say we wanted to add a function for printing out the grade for a single student. We already have a function which determines the student's grade, so we can use this in our new function:

def get_grade(student_name, weekly_points):
    for name, point_list in weekly_points.items():
        if name == student_name:
            return grade(sum(point_list))

weekly_points = read_weekly_points("weekly_points.csv")
print(get_grade("Paula", weekly_points))
