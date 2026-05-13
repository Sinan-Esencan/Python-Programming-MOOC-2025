# The exercise template contains a class named Car which represents the features of a car through two attributes: make (str) and top_speed (int).
# Please write a function named fastest_car(cars: list) which takes a list of Car objects as its argument.
# The function should return the make of the fastest car. You may assume there will always be a single car with the highest top speed. Do not change the list given as an argument, or make any changes to the Car class definition.


# Write your solution after the class Car
# Do not make changes to the class!
class Car:
    def __init__(self, make: str, top_speed: int):
        self.make = make
        self.top_speed = top_speed        

    def __str__(self):
        return f"Car (make: {self.make}, top speed: {self.top_speed})"

# WRITE YOUR SOLUTION HERE:

def fastest_car(cars: list):
    car_with_top_speed = cars[0]
    for car in cars:
        if car.top_speed > car_with_top_speed.top_speed:
            car_with_top_speed = car
    return car_with_top_speed.make

# alt: karısık ve kotu versiyon:
# def fastest_car(cars: list):
#     car_with_top_speed = None
#     top_speed = 0
#     for car in cars:
#         if car.top_speed > top_speed:
#             top_speed = car.top_speed
#             car_with_top_speed = car
#     return car_with_top_speed.make

# alt2:- mooc.fi alternatifi ve guzel:
# def fastest_car(cars: list):
#     fastest_make = cars[0].make
#     best_speed = cars[0].top_speed
#     for car in cars:
#         if car.top_speed > best_speed:
#             best_speed = car.top_speed
#             fastest_make = car.make
#     return fastest_make

if __name__ == "__main__":
    car1 = Car("Saab", 195)
    car2 = Car("Lada", 110)
    car3 = Car("Ferrari", 280)
    car4 = Car("Trabant", 85)

    cars = [car1, car2, car3, car4]
    print(fastest_car(cars))
