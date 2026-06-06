# The database of a real estate agency keeps records of available properties with objects defined by the following class:
# Your task is to implement methods which allow for comparison between available properties.
# Devamı için Advanced Course in Programming > Part 9 > Objects and References > Comparing Properties

class RealProperty:
    def __init__(self, rooms: int , square_metres: int , price_per_sqm:int):
        self.rooms = rooms
        self.square_metres = square_metres
        self.price_per_sqm = price_per_sqm
    
    def bigger(self, compared_to):
        return self.square_metres > compared_to.square_metres

    def price_difference(self, compared_to):
        return abs(self.square_metres*self.price_per_sqm - compared_to.square_metres*compared_to.price_per_sqm)

    def more_expensive(self, compared_to):
        difference = self.square_metres*self.price_per_sqm - compared_to.square_metres*compared_to.price_per_sqm
        return difference > 0

if __name__ == "__main__":
    central_studio = RealProperty(1, 16, 5500)
    downtown_two_bedroom = RealProperty(2, 38, 4200)
    suburbs_three_bedroom = RealProperty(3, 78, 2500)

    #1
    print(central_studio.bigger(downtown_two_bedroom))
    print(suburbs_three_bedroom.bigger(downtown_two_bedroom))

    #2
    print(central_studio.price_difference(downtown_two_bedroom))
    print(suburbs_three_bedroom.price_difference(downtown_two_bedroom))

    #3
    print(central_studio.more_expensive(downtown_two_bedroom))
    print(suburbs_three_bedroom.more_expensive(downtown_two_bedroom))
