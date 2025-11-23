def read_fruits():
    with open("fruits.csv") as new_file:
        fruits_and_prices = {}
        for line in new_file:
            line = line.replace("\n", "") #alt: line.strip()
            parts = line.split(";")
            # print(parts)
            fruit = parts[0]
            price = float(parts[1])
            fruits_and_prices[fruit] = price           
        return fruits_and_prices

if __name__ == "__main__":
    print(read_fruits())


# alt1 - mooc.fi:
def read_fruits():
    with open("fruits.csv") as file:
        fruits = {}
        for row in file:
            data = row.split(";")
# split() fonksiyonundan once replace() veya strip() kullanılmamıs cunku int() gibi float() da white space'i otomatik temizler
            fruits[data[0]] = float(data[1])
    return fruits


#alt2: using csv module:
import csv

def read_fruits():
    with open("fruits.csv") as my_file:
        fruits_and_prices = {}
        for parts in csv.reader(my_file, delimiter=";"):
            # print(parts)
            fruit = parts[0]
            price = float(parts[1])
            fruits_and_prices[fruit] = price
        return fruits_and_prices
