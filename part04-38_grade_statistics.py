def exercise_point_calculator():
    list_pointsduo = []
    while True:
        points = input("Exam points and exercises completed: ")
        if points == "":
            return list_pointsduo
        try:
            x, y = points.split()
            list_pointsduo.append([int(x),int(y)])
            #alt: ValueError yerine IndexError demek sartıyla:
            #lst = points.split()
            #list_pointsduo.append([int(lst[0]),int(lst[1])])
#list_pointsduo.append(list(points.split())) veya list_pointsduo.append(points.split()) denseydi cevap aynı olurdu ve notları int'e cevirmezdi
#ancak tur degistirme islemini map() ile yapsak o zaman list()'in onemi olurdu: list_pointsduo.append(list(map(int, points.split()))) -bkz asagıdaki alt-
        except ValueError:
            print("Enter Valid number!")

    
def grade_calculator(list_pointsduo:list):
    grade_list = []
    total_points_list = []
    for pointsduo in list_pointsduo:
        grade = 0
        exercise_points = pointsduo[1]//10
        total_points = pointsduo[0] + exercise_points
        total_points_list.append(total_points)

        if pointsduo[0] < 10:
            grade = 0
        else:
            if total_points <= 14:
                grade = 0
            elif total_points <= 17:
                grade = 1
            elif total_points <= 20:
                grade = 2
            elif total_points <= 23:
                grade = 3
            elif total_points <= 27:
                grade = 4
            elif total_points <= 30:
                grade = 5
        grade_list.append(grade)

    average_point = average_point_calculator(total_points_list)
    return grade_list, average_point

def average_point_calculator(total_points_list:list):
    return round(sum(total_points_list)/len(total_points_list),1)
# return etmek yerine global variable yaratılabilirdi


def grade_distribution(grade_list, average_point):
    failed = 0
    total = len(grade_list)
    for grade in grade_list:
        if grade == 0:
            failed += 1
    print("Statistics:")
    print("Points average:", average_point)
    print("Pass percentage:", round(((total-failed)/total*100),1))
#alt: print("Pass percentage:", f"{((total-failed)/total*100):.1f}")
    print("Grade distribution:")
    for i in range(5,-1,-1):
        print(f"{i}: {grade_list.count(i) * '*'}") #bu kısmı bulmam zor oldu


def main():
    list_pointsduo = exercise_point_calculator()
    grade_list, average_point = grade_calculator(list_pointsduo)
    grade_distribution(grade_list, average_point)

main() #normalde if __name__ == "__main__": blok icerisinde


#3 FONKSIYON ICIN 3 AYRI UNIT TESTING YAPTIM ILK BASTA:
# list_pointsduo = exercise_point_calculator()
# grade_list, average_point = grade_calculator([[15, 87],[10, 55],[11, 40], [4, 17]])
# grade_distribution([3, 1, 1, 0], 14.5)



#V2: map() kullanmak cok fazla conversion varsa pratiklik saglar:
def exercise_point_calculator():
    list_pointsduo = []
    while True:
        points = input("Exam points and exercises completed: ")
        if points == "":
            return list_pointsduo
        try:
            x, y = map(int, points.split())
            list_pointsduo.append([x,y])
#alt: list_pointsduo.append(list(map(int, points.split())))            
#alt2: tamamen parcalayarak:
# parcalar = points.split()
# pieces = map(int, parcalar)
# list_pointsduo.append(list(pieces))            
        except ValueError:
            print("Enter Valid number!")
