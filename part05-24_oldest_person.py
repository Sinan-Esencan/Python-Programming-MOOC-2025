# Please write a function named oldest_person(people: list), which takes a list of tuples as its argument. In each tuple, the first element is the name of a person, 
# and the second element is their year of birth. The function should find the oldest person on the list and return their name.

def oldest_person(people: list):
    oldest = people[0][1]
    oldest_person = people[0][0]
    for person in people:
        if person[1] < oldest:
            oldest = person[1]
            oldest_person = person[0]
    return oldest_person

if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]
    print(oldest_person(people))
    # people_list = [('Arthur', 1977), ('Emily', 2014)]
    # print(oldest_person(people_list))


# alt2 - mooc.fi: daha efektif ve tek dictionary objede toplamıs:
def oldest_person(people: list):
    oldest = people[0]
    for person in people:
        # comparing the year of birth of the oldest known person and the person in turn
        if person[1] < oldest[1]:
            oldest = person
    return oldest[0]
