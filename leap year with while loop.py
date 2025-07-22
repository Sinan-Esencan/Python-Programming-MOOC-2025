first_year = int(input("Year: "))
year = first_year
leap_year = False

while True:
    year += 1

    if year % 4 == 0 and year % 100 != 0:
        leap_year = True
        break
    elif year % 400 == 0:
        leap_year = True
        break
        
''' alt:
    if year % 100 == 0 and year % 400 == 0 :
        leap_year = True
        break
    elif year % 4 == 0 and year % 100 != 0:
        leap_year = True
        break
'''

""" alt2:
    if year % 100 == 0:
        if year % 400 == 0:
            break
    elif year % 4 == 0:
        break
"""

print(f"The next leap year after {first_year} is {year}")
