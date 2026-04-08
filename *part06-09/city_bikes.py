# In this exercise we will write some functions for working on a file containing location data from the stations for city bikes in Helsinki.
# Each file will follow this format:
# Longitude;Latitude;FID;name;total_slot;operative;id
# 24.950292890004903;60.155444793742276;1;Kaivopuisto;30;Yes;001
# 24.956347471358754;60.160959093887129;2;Laivasillankatu;12;Yes;002
# 24.944927399779715;60.158189199971673;3;Kapteeninpuistikko;16;Yes;003
# Each station has a single line in the file. The line contains the coordinates, name, and other identifying information for the station.

# part1: Distance between stations
First, write a function named get_station_data(filename: str). This function should read the names and locations of all the stations in the file, and return them in a dictionary with the following format:

Sample output
{
  "Kaivopuisto": (24.950292890004903, 60.155444793742276),
  "Laivasillankatu": (24.956347471358754, 60.160959093887129),
  "Kapteeninpuistikko": (24.944927399779715, 60.158189199971673)
}
Dictionary keys are the names of the stations, and the value attached is a tuple containing the location coordinates of the station. The first element in the tuple is the Longitude field, and the second is the Latitude field.
Next, write a function named distance(stations: dict, station1: str, station2: str), which returns the distance between the two stations given as arguments.
The distance is calculated using the Pythagorean theorem. The multiplication factors below are approximate values for converting latitudes and longitudes to distances in kilometres in the Helsinki region.

# we will need the function sqrt from the math module 
import math
x_km = (longitude1 - longitude2) * 55.26
y_km = (latitude1 - latitude2) * 111.2
distance_km = math.sqrt(x_km**2 + y_km**2)

Some examples of the function in action:

stations = get_station_data('stations1.csv')
d = distance(stations, "Designmuseo", "Hietalahdentori")
print(d)
d = distance(stations, "Viiskulma", "Kaivopuisto")
print(d)

Sample output
0.9032737292463177
0.7753594392019532

part2: The greatest distance

Please write a function named greatest_distance(stations: dict), which works out the two stations on the list with the greatest distance from each other. The function should return a tuple, where the first two elements are the names of the two stations, and the third element is the distance between the two.

stations = get_station_data('stations1.csv')
station1, station2, greatest = greatest_distance(stations)
print(station1, station2, greatest)

Sample output
Laivasillankatu Hietalahdentori 1.478708873076181




def get_station_data(filename: str):
    station_coordinates = {}
    with open(filename) as new_file:
        title = next(new_file) #title atlamak icin
        for line in new_file:
            line = line.strip()
            parts = line.split(";")
# alt: clean_line = line.strip().split(";")
            name = parts[3]
            longitude = float(parts[0]) #float demeyi unutma
            latitude= float(parts[1])
            station_coordinates[name] = (longitude, latitude)
# *station_coordinates[name,1] = (longitude, latitude) deseydim her key tuple olacaktı ve tuple olusturmak
# icin (arguman olarak pass etmeyeceksen) paranteze gerek olmadıgını, virgule gerek oldugunu unutma*
    return station_coordinates

def distance(stations: dict, station1: str, station2: str):
    # coordinates1  = stations[station1]
    # longitude1 = coordinates1[0]
    # latitude1 = coordinates1[1]
    # coordinates2  = stations[station2]
    # longitude2 = coordinates2[0]
    # latitude2 = coordinates2[1]
    # yukarıdaki gibi uzatacagıma dogrudan tuple destructuring yapmalıyım:
    longitude1, latitude1 = stations[station1]
    longitude2, latitude2 = stations[station2]


    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km

def greatest_distance(stations: dict):
    greatest_distance_km = 0
    # *python'da java'daki gibi variable declaration zorunluluğu yok:*
    # distant_station1 = ""
    # distant_station2 = ""
    for station1 in stations: #alt: stations.keys()
        for station2 in stations:
            distance_km = distance(stations, station1, station2)
            if distance_km > greatest_distance_km:
                greatest_distance_km = distance_km
                distant_station1 = station1
                distant_station2 = station2
                # print(greatest_distance_km, distant_station1, distant_station2)
            # print(station1, station2, distance_km)
    return distant_station1, distant_station2, greatest_distance_km

if __name__ == "__main__":
    # 1
    # stations = get_station_data('stations1.csv')
    # # print(stations)
    # d = distance(stations, "Designmuseo", "Hietalahdentori")
    # print(f"{d:.12f}")
    # d = distance(stations, "Viiskulma", "Kaivopuisto")
    # print(f"{d:.12f}")

    #2
    stations = get_station_data('stations1.csv')
    # greatest_distance(stations)
    station1, station2, greatest = greatest_distance(stations) #returns a tuple
    print(station1, station2, greatest)
    # print(f"Longest distance is between stations {station1} and {station2}")
