# Please write a function named lottery_numbers(amount: int, lower: int, upper: int), which generates as many random numbers as specified by the first argument. All numbers should fall within the bounds lower to upper. The numbers should be stored in a list and returned. The numbers should be in ascending order in the returned list.
# As these are lottery numbers, no number should appear twice in the list.
# An example of how the function should work:
# for number in lottery_numbers(7, 1, 40):
#     print(number)
# Sample output
# 4
# 7
# 11
# 16
# 22
# 29
# 38

import random

def lottery_numbers(amount: int, lower: int, upper: int):
    #ise yaramaz cunku aynı sayılar cıkabiliyor:
    # lottery = []
    # for x in range(amount):
    #     lottery.append(random.randint(lower, upper))
    # return sorted(lottery)

    # alt1:
    # lottery = []
    # while len(lottery) < amount :
    #     number = random.randint(lower, upper)
    #     if number not in lottery:
    #         lottery.append(number)
    # return sorted(lottery)

    # alt2:
    # number_pool = list(range(lower, upper))
    # random.shuffle(number_pool)
    # weekly_draw = number_pool[0:amount]
    # return sorted(weekly_draw)
    
    # alt3: en kolay versiyon:
    number_pool = list(range(lower, upper))
    weekly_draw = random.sample(number_pool,amount) #weekly_draw listtir
    return sorted(weekly_draw)


if __name__ == "__main__":
    for number in lottery_numbers(7, 1, 40):
        print(number)
