#Please write a program which asks the user to type in a limit. The program then calculates the sum of consecutive numbers (1 + 2 + 3 + ...) until the sum is at 
#least equal to the limit set by the user. The program should function as follows. In addition to the result it should also print out the calculation performed

#V1:
limit = int(input("Limit: "))
i = 1
total = 0
indexes = "0"

while total < limit:
    indexes += f" + {i}"
    total += i
    i +=1

print("The consecutive sum:", indexes, "=", total) #fazladan sıfır print eder


#V2:
limit = int(input("Limit: "))
i = 1
indexes=""
sum = 1
while sum < limit:
    indexes += f"{i} + "
    i += 1
    sum += i
indexes += f"{i}"
print(f"The consecutive sum: {indexes} = {sum}")


#V3: sitenin:
limit = int(input("Limit: "))
number = 1
sum = 1
numbers = "1"

while sum < limit:
    number += 1
    sum += number
    numbers += f" + {number}"

print(f"The consecutive sum: {numbers} = {sum}")
