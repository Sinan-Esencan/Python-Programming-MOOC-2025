# The exercise template contains the class Person. A person has a name and a height. In this exercise you will implement the class Room. You may add any number of persons to a room, and you may also search for and remove the shortest person in the room.
# Part1: Please define the class Room. It should have a list of persons as an attribute, and also contain the following methods:
#     add(person: Person) adds the person given as an argument to the room.
#     is_empty() returns True or False depending on whether the room is empty.
#     print_contents() prints out the contents of the list of persons in the room.

# Part2: The shortest person
# Please define the method shortest() within the Room class definition. The method should return the shortest person in the room it is called on.
# If the room is empty, the method should return None. The method should not remove the person fron the room.

# Part3: Removing a person from the room
# Please define the method remove_shortest() within the Room class definition. The method should remove the shortest Person object from the room
# and return the reference to the object. If the room is empty, the method should return None.

class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.list_person = []

    def add(self, person: Person):
        self.list_person.append(person)
    
    def is_empty(self): 
        return len(self.list_person) == 0
        # alt: return not self.list_person
    
    def print_contents(self):
        total_height = 0
        for person in self.list_person:
            total_height += person.height

        print(f"There are {len(self.list_person)} persons in the room, and their combined height is {total_height} cm")
        for person in self.list_person:
            print(f"{person} ({person.height} cm)")

    def shortest(self):
        if len(self.list_person) == 0:
            return None
        shortest = self.list_person[0]
        for person in self.list_person:
            if person.height < shortest.height:
                shortest = person
        return shortest

    def remove_shortest(self):
        try:
            shortest_person = self.shortest()
            self.list_person.remove(shortest_person)
            return shortest_person
        except ValueError:
            return None
    # *bu metodun daha duzgun yazılmıs hali:*
        # shortest_person = self.shortest()
        # if shortest_person:
        #     self.list_person.remove(shortest_person)
        # return shortest_person

if __name__ == "__main__":
    # 1
    # room = Room()
    # print("Is the room empty?", room.is_empty())
    # room.add(Person("Lea", 183))
    # room.add(Person("Kenya", 172))
    # room.add(Person("Ally", 166))
    # room.add(Person("Nina", 162))
    # room.add(Person("Dorothy", 155))
    # print("Is the room empty?", room.is_empty())
    # room.print_contents()

    # 2
    # room = Room()
    # print("Is the room empty?", room.is_empty())
    # print("Shortest:", room.shortest())
    
    # room.add(Person("Lea", 183))
    # room.add(Person("Kenya", 172))
    # room.add(Person("Nina", 162))
    # room.add(Person("Ally", 166))
    # print("Is the room empty?", room.is_empty())
    # print("Shortest:", room.shortest())
    # room.print_contents()

    # 3
    room = Room()

    removed = room.remove_shortest()
    if removed is not None:
        print(f"Removed from room: {removed.name}")
    room.print_contents()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    removed = room.remove_shortest()
    if removed is not None:
        print(f"Removed from room: {removed.name}")
    room.print_contents()
