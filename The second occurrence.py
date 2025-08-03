#Please write a program which finds the second occurrence of a substring. If there is no second (or first) occurrence, the program should print out a message accordingly.
#In this exercise the occurrences cannot overlap. For example, in the string aaaa the second occurrence of the substring aa is at index 2.

text = input("Please type in a string: ")
substring = input("Please type in a substring: ")
first_index = text.find(substring)

if first_index == -1:
#bu kısım opsiyonel ama guzel cunku ilk aramada yoksa zaten ikincide de yoktur
    print("The substring does not occur twice in the string.")
else:
    second_index = text.find(substring, first_index + len(substring))
    if second_index == -1:
        print("The substring does not occur twice in the string.")
    else:
        print(f"The second occurrence of the substring is at index {second_index}.")

#alt2: mooc alternatifinde text[].find kullanıldıgı icin biraz daha farklı:
string = input("Please type in a string: ")
substring = input("Please type in a substring: ")
index1 = string.find(substring)
index2 = -1
if index1 != -1:
    string = string[index1+len(substring):]
    index2 = string.find(substring)

if index2 == -1:
    print("The substring does not occur twice in the string.")
else:
    print("The second occurrence of the substring is at index " + str(index1+len(substring)+index2) +  ".")
