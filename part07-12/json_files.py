# Let's have a look at a JSON file, which contains some information about students in the following format:

# [
#     {
#         "name": "Peter Pythons",
#         "age": 27,
#         "hobbies": [
#             "coding",
#             "knitting"
#         ]
#     },
#     {
#         "name": "Jean Javanese",
#         "age": 24,
#         "hobbies": [
#             "coding",
#             "rock climbing",
#             "reading"
#         ]
#     }
# ]

# Please write a function named print_persons(filename: str), which reads a JSON file in the above format, and prints the contents as shown below. The file may contain any number of entries:
# Peter Pythons 27 years (coding, knitting)
# Jean Javanese 24 years (coding, rock climbing, reading)

# The hobbies should be listed in the same order as they appear in the JSON file.

import json

def print_persons(filename: str):
    with open(filename) as my_file:
        data = my_file.read()
    # print(data)
    person_list = json.loads(data)
    # print(person_list)
    for person in person_list:
        # print(person)
        hobbies = ", ".join(person['hobbies'])
        print(f"{person['name']} {person['age']} years ({hobbies})")

if __name__ == "__main__":
    print_persons("file1.json")
