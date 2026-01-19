# Please write a function named smallest_average(person1: dict, person2: dict, person3: dict), which takes three dictionary objects as its arguments.

# Each dictionary object contains values mapped to the following keys:

#     "name": The name of the contestant
#     "result1": the first result of the contestant (an integer between 1 and 10)
#     "result2": the second result of the contestant (as above)
#     "result3": the third result of the contestant (as above)

# The function should calculate the average of the three results for each contestant, and then return the contestant whose average result was the smallest. The return value should be the entire dictionary object containing the contestant's information.

# You may assume there will be no ties, i.e. a single contestant will have the smallest average result.

# An example of the function in action:

# person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
# person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
# person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

# print(smallest_average(person1, person2, person3))

# Sample output

# {'name': 'Larry', 'result1': 3, 'result2': 1, 'result3': 1}

def smallest_average(person1: dict, person2: dict, person3: dict):
    min_obj = person1
    min = person1["result1"] + person1["result2"] + person1["result3"]

    if (person2["result1"] + person2["result2"] + person2["result3"]) < min:
        min_obj = person2
        min = person2["result1"] + person2["result2"] + person2["result3"]

    if (person3["result1"] + person3["result2"] + person3["result3"]) < min:
        min_obj = person3
        min = person3["result1"] + person3["result2"] + person3["result3"]

    return min_obj
    
if __name__ == "__main__":
    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}
    print(smallest_average(person1, person2, person3))


# alt1 - mooc.fi: better version:
def average(person: dict):
    ex_sum = person["result1"]+person["result2"]+person["result3"]
    return ex_sum/3

def smallest_average(person1: dict, person2: dict, person3: dict):
    smallest = person1

    if average(person2) < average(smallest):
        smallest = person2

    if average(person3) < average(smallest):
        smallest = person3

    return smallest


# alt2: 3 kisi oldugunu biliyorsak ama her kisinin result sayısını bilmiyorsak:
def average(person: dict):
    results = []
    # Sadece "result" ile başlayan anahtarları al
    for key in person:
        if key.startswith("result"):
            results.append(person[key])
            
    return sum(results) / len(results)

def smallest_average(person1: dict, person2: dict, person3: dict):
    smallest = person1

    if average(person2) < average(smallest):
        smallest = person2

    if average(person3) < average(smallest):
        smallest = person3

    return smallest

if __name__ == "__main__":
    person1 = {"name": "Mary", "result1": 2, "result2": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}
    print(smallest_average(person1, person2, person3))


# alt3: kac kisi oldugunu bilmiyorsak tuple (demet) icerisinde person objelerini toplar ve looplarız:
def average(person: dict):
    results = []
    for key in person:
        if key.startswith("result"):
            results.append(person[key])
    return sum(results) / len(results)

# *person ile gelen tüm kişileri bir tuple olarak alıyoruz
def smallest_average(*person):
    smallest = person[0] # Başlangıç olarak ilk kişiyi alıyoruz

    # Tuple içindeki her bir kişiyi (p) sırayla gez
    for p in person:
        if average(p) < average(smallest):
            smallest = p
            
    return smallest
