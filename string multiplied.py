#V1: shorter:
input_string = input("Please type in a string: ")
amount = int(input("Please type in an amount: "))
print (input_string * amount)


#V2:
string = input("Please type in a string: ")
times = int(input("Please type in an amount: "))
n = 1
combined = ""

while n <= times:
    combined += string
    n += 1

print(combined)


