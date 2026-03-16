# part1: Count the numbers
# Please write a class named NumberStats with the following methods:
#     the method add_number adds a new number to the statistical record
#     the method count_numbers returns the count of how many numbers have been added
# At this point there is no need to store the numbers themselves in any data structure. It is enough to simply remember how many have been added. The add_number method does take an argument, but there is no need to process the actual value in any way just yet.
# part2: The sum and the mean
# Please add the following methods to your class definition:
#     the method get_sum should return the sum of the numbers added (if no numbers have been added, the method should return 0)
#     the method average should return the mean of the numbers added (if no numbers have been added, the method should return 0)
# part3: User input
# Please write a main program which keeps asking the user for integer numbers until the user types in -1. The program should then print out the sum and the mean of the numbers typed in.
# Your program should use a NumberStats object to keep a record of the numbers added.
# NB: you do not need to change the NumberStats class in this part of the exercise, provided it passed the tests for the previous part of the exercise. Use an instance of the class to complete this part.
# NB2: your main program should not be contained in a if __name__ == "__main__" block, or the tests will not work.
# part4: Multiple sums
# Please add to your main program so that it also counts separately the sum of the even and the odd numbers added.
# NB: do not change your NumberStats class definition in this part of exercise, either. Instead, define three NumberStats objects. One of them should keep track of all the numbers, another should track the even numbers, and the third should track the odd numbers typed in.
# NB2: your main program should not be contained in a if __name__ == "__main__" block, or the tests will not work.

# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.total = 0

    def add_number(self, number:int):
        self.numbers += 1
        self.total += number

    def count_numbers(self):
        return self.numbers

    def get_sum(self):
        return self.total

    def average(self):
        if self.numbers == 0:
            return 0
        return self.get_sum() / self.count_numbers()
        # alt1: ternary operator: return self.total / self.numbers if self.numbers else 0
        # alt2: try except (exceptionlar beklenmedik hatalar icin tasarlandıgından kotu tercih!): 
        # try:
        #     return self.total/self.numbers
        # except ZeroDivisionError:
        #     return 0


# # 1
# stats = NumberStats()
# stats.add_number(3)
# stats.add_number(5)
# stats.add_number(1)
# stats.add_number(2)
# print("Numbers added:", stats.count_numbers())

# #2
# stats = NumberStats()
# stats.add_number(3)
# stats.add_number(5)
# stats.add_number(1)
# stats.add_number(2)
# print("Numbers added:", stats.count_numbers())
# print("Sum of numbers:", stats.get_sum())
# print("Mean of numbers:", stats.average())

# 3
# stats = NumberStats()
# print("Please type in integer numbers:")
# while True:
#     number = int(input())
#     if number == -1:
#         print("Sum of numbers:", stats.get_sum())
#         print("Mean of numbers:", stats.average())
#         break
#     stats.add_number(number)

# # alt: Awkward alternative — requires a dummy initial value
# stats = NumberStats()
# print("Please type in integer numbers:")
# number = 0
# while number != -1:
#     number = int(input())
#     if number != -1:  # second check needed to avoid adding -1
# # The `while True` + `break` version avoids this entirely by checking 
# # the condition immediately after input, before any processing.
#         stats.add_number(number)
# print("Sum of numbers:", stats.get_sum())
# print("Mean of numbers:", stats.average())

# 4
all_numbers = NumberStats()
even_numbers = NumberStats()
odd_numbers = NumberStats()
print("Please type in integer numbers:")
while True:
    number = int(input())
    if number == -1:
        break
    
    if number % 2:
        odd_numbers.add_number(number)
    else:
        even_numbers.add_number(number)
    all_numbers.add_number(number)

print("Sum of numbers:",all_numbers.get_sum())
print("Mean of numbers:",all_numbers.average())
print("Sum of even numbers:",even_numbers.get_sum())
print("Sum of odd numbers:",odd_numbers.get_sum())


# alt - mooc.fi: array kullanarak hem degerlerin toplamına hem de counter sayısına ulasılabilir:
class  NumberStats:
    def __init__(self):
        self.numbers = []
 
    def add_number(self, number:int):
        self.numbers.append(number)
 
    def count_numbers(self):
        return len(self.numbers)
 
    def get_sum(self):
        return sum(self.numbers)
 
    def average(self):
        if not self.numbers:
            return 0.0
        else:
            return self.get_sum() / self.count_numbers()
 
stats = NumberStats()
even = NumberStats()
odd = NumberStats()
while True:
    number = int(input("Give a number: "))
    if number == -1:
        break
 
    stats.add_number(number)
    if number % 2 == 0:
        even.add_number(number)
    else:
        odd.add_number(number)
 
print("Sum of numbers:", stats.get_sum())
print("Mean of numbers:", stats.average())
print("Sum of even numbers:", even.get_sum())
print("Sum of odd numbers:", odd.get_sum())
