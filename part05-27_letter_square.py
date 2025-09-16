# This final exercise in this part is a relatively demanding problem solving task. It can be solved in many different ways. Even though this current section in the material covers tuples, tuples are not necessarily the best way to go about solving this.
# Please write a program which prints out a square of letters as specified in the examples below. You may assume there will be at most 26 layers.
# Layers: 3
# CCCCC
# CBBBC
# CBABC
# CBBBC
# CCCCC
# Layers: 4
# DDDDDDD
# DCCCCCD
# DCBBBCD
# DCBABCD
# DCBBBCD
# DCCCCCD
# DDDDDDD

import string
harfler = {i: letter for i, letter in enumerate(string.ascii_uppercase, 0)} #dictionary comprehension
#list comprehension: new_list = [x * 2 for x in numbers]
#veya: harfler = [letter for i, letter in enumerate(string.ascii_lowercase, 0)]

layers = int(input("Layers: "))
rows = 2*layers-1
cols = rows
matrix = []
new_list = []
center_y = rows//2 #alt: center_y = layers - 1
center_x = cols//2
for y in range(rows):
    new_row = []
    for x in range(cols):
        distance = max(abs(y-center_y), abs(x-center_x))
        print(harfler[distance], end="")
    print()

#ustunden gittigim basit ornek: Layers: 3
# CCCCC
# CBBBC
# CBABC
# CBBBC
# CCCCC

#V2: storing values in a list instead of printing immediately:
import string
harfler = {i: letter for i, letter in enumerate(string.ascii_uppercase, 0)} #dictionary comprehension
layers = int(input("Layers: "))
rows = 2*layers-1
cols = rows
matrix = []
new_list = []
center_y = rows//2
center_x = cols//2
for y in range(rows):
    new_row = []
    for x in range(cols):
        distance = max(abs(y-center_y), abs(x-center_x))
        new_row.append(harfler[distance])
    matrix.append(new_row)
# daha once 2d arrayde for in loop kullanılınca izlenen yol:
#     new_list = []
#     for row in old_list:
#         new_row = []  # Her satır için yeni bir liste oluştur
#         for square in row:
#             new_row.append(square)  # Her kareyi yeni satıra ekle
#         new_list.append(new_row)  # Yeni satırı ana listeye ekle

for row in matrix:
    for char in row:
        print(char, end="")
    print()


#V3 - mooc.fi cozumu ama benimki daha iyiymis:
n = int(input("Layers: "))
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
left = ""    # section, that goes downwards
right = ""    # section, that goes upwards
k = n-1       # the location of next character in alphabets
m = 2*n-1     # the number of characters in between
while k >= 1:
    left = left+alphabets[k]
    right = alphabets[k]+right
    m -= 2
    print(left+alphabets[k]*m+right)
    k -= 1
while k <= n-1:
    print(left+alphabets[k]*m+right)
    left = left[:-1]
    right = right[1:]
    m += 2
    k += 1
