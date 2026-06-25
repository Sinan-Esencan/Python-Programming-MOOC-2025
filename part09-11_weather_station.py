# Please create a class named WeatherStation which is used to store observations about the weather. The class should have the following public attributes:
#     a constructor which takes the name of the station as its argument
#     a method named add_observation(observation: str) which adds an observation as the last entry in a list
#     a method named latest_observation() which returns the latest observation added to the list. If there are no observations yet, the method should return an empty string.
#     a method named number_of_observations() which returns the total number of observations added
#     a __str__ method which returns the name of the station and the total number of observations added as per the example below.
# All attributes should be encapsulated, so they can't be directly accessed. It is up to you how you implement the class, as long as the public interface is exactly as described above.

class WeatherStation:
    def __init__(self, station_name):
        self.__station_name = station_name
        self.__observations = []

    def add_observation(self, observation: str):
        self.__observations.append(observation)
    
    def latest_observation(self):
        if len(self.__observations) > 0:
            return self.__observations [len(self.__observations)-1]
        else:
            raise ValueError("list index out of range")
    
    def number_of_observations(self):
        return len(self.__observations)
    
    def __str__(self):
        return f"{self.__station_name}, {self.number_of_observations()} observations"

if __name__ == "__main__":
    try:
        station = WeatherStation("Houston")
        station.add_observation("Rain 10mm")
        station.add_observation("Sunny")
        print(station.latest_observation())

        station.add_observation("Thunderstorm")
        print(station.latest_observation())

        print(station.number_of_observations())
        print(station)
    except ValueError as e:
        print(e)

# alt: mooc.fi - better version: valueerror throw etmedigimdem try except bloga gerek kalmadı:
class WeatherStation:
    def __init__(self, station_name):
        self.__station_name = station_name
        self.__latest_observation = ""
        self.__observation_number = 0

    def add_observation(self, observation: str):
        self.__latest_observation = observation
        self.__observation_number += 1
    
    def latest_observation(self):
        return self.__latest_observation
    
    def number_of_observations(self):
        return self.__observation_number
    
    def __str__(self):
        return f"{self.__station_name}, {self.number_of_observations()} observations"
