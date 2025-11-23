# part1: Retrieving the list of active courses
# At the address https://studies.cs.helsinki.fi/stats-mock/api/courses you will find basic information about some of the courses offered by the University of Helsinki Department of Computer Science, in JSON format.

# Please write a function named retrieve_all(), which retrieves the data of all the courses which are currently active (the field enabled has the value true). These should be returned as a list of tuples, in the following format:
# Sample output

# [
#     ('Full Stack Open 2020', 'ofs2019', 2020, 201),
#     ('DevOps with Docker 2019', 'docker2019', 2019, 36),
#     ('DevOps with Docker 2020', 'docker2020', 2020, 36),
#     ('Beta DevOps with Kubernetes', 'beta-dwk-20', 2020, 28)
# ]

# Each tuple contains the following fields from the original data:

#     the name of the course: fullName
#     name
#     year
#     the sum of the values listed in exercises

# part2: Retrieving the data for a single course
# Each course also has its own URL, where more specific weekly data about the course is available. The URLs follow the format https://studies.cs.helsinki.fi/stats-mock/api/courses/****/stats, where you would replace the stars with the contents of the field name for the course you want to access.

# For example, the data for the course docker2019 is at the address https://studies.cs.helsinki.fi/stats-mock/api/courses/docker2019/stats.

# Please write a function named retrieve_course(course_name: str), which returns statistics for the specified course, in dictionary format.

# For example, the function call retrieve_course("docker2019") would return a dictionary with the following contents:
# Sample output

# {
#     'weeks': 4,
#     'students': 220,
#     'hours': 5966,
#     'hours_average': 27,
#     'exercises': 4988,
#     'exercises_average': 22
# }

# The values in the dictionary are determined as follows:

#     weeks: the number of JSON object literals retrieved
#     students: the maximum number of students in all the weeks
#     hours: the sum of all hour_total values in the different weeks
#     hours_average: the hours value divided by the students value (rounded down to the closest integer value)
#     exercises: the sum of all exercise_total values in the different weeks
#     exercises_average: the exercises value divided by the students value (rounded down to the closest integer value)

import json, urllib.request, math

def retrieve_all():
    request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    data = request.read()
    course_data = json.loads(data)#loads() transforms json data to a readable format
    # print(course_data,"\n")
    lessons = []
    for lesson in course_data:
        # print("lesson", lesson)
        if lesson['enabled'] == True:
            lessons.append((lesson['fullName'], lesson['name'], lesson['year'], sum(lesson['exercises'])))
    return lessons


def retrieve_course(course_name: str):
    request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses/"+course_name+"/stats")
    data = request.read()
    weekly_course_data = json.loads(data)
    # print(weekly_course_data)
    lesson_dict = {}
    students_by_weeks = []
    sum_of_hour_total = 0
    sum_of_exercise_total = 0
    for week, value in weekly_course_data.items():
        students_by_weeks.append(value["students"])
        sum_of_hour_total += value["hour_total"]
        sum_of_exercise_total += value["exercise_total"]

    lesson_dict["weeks"] = len(weekly_course_data)
    lesson_dict["students"] = max(students_by_weeks)
    lesson_dict["hours"] = sum_of_hour_total  
    lesson_dict["hours_average"] = math.floor(lesson_dict["hours"]/lesson_dict["students"]) #approx total hours per student
    lesson_dict["exercises"] = sum_of_exercise_total
    lesson_dict["exercises_average"] = math.floor(lesson_dict["exercises"]/lesson_dict["students"])
    
    return lesson_dict


if __name__ == "__main__":
    print(retrieve_all())
    print(retrieve_course("docker2019"))

