# soru icin: part 9 > More examples with classes > Item, Suitcase and Cargo hold

class Item:
    def __init__(self, name: str, weight: float):
        self.__name = name
        self.__weight = weight

    def name(self) -> str:
        return self.__name

    def weight(self) -> float:
        return self.__weight

    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"


class Suitcase:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.items = []

    def weight(self):
        return sum(item.weight() for item in self.items)

    def add_item(self, item: Item):
        if self.weight() + item.weight() <= self.__max_weight:
            self.items.append(item)

    def print_items(self):
        for item in self.items:
            print(item)

    def heaviest_item(self):
        # ilk bastaki yanlıs uygulamam (obje return etmeliymisim)
        # max_weight = max(((item.weight(), item.name()) for item in self.items), default=None)
        # return f"{max_weight[1]} ({max_weight[0]} kg)"
        max_item = None
        for item in self.items:
            if max_item is None or item.weight() > max_item.weight():
                max_item = item
        return max_item

    def __str__(self):
        # total_weight = sum(item.weight() for item in self.items)
        return (
            f"{len(self.items)} "
            f"{'item ' if len(self.items) == 1 else 'items '}"
            f"({self.weight()} kg)"
        #*alt:* f"({sum(map(lambda item: item.weight(), self.items))} kg)"
        )


class CargoHold:
    def __init__(self, max_weight):
        self.suitcases: Suitcase = []
        self._max_weight = max_weight
    
    def weight(self):
        return sum(suitcase.weight() for suitcase in self.suitcases) 
    
    def add_suitcase(self, suitcase: Suitcase):
        #if listedeki combined bavul weight + eklenecek bavul weight <= sınır:
        if self.weight() + suitcase.weight() <= self._max_weight:
            self.suitcases.append(suitcase)

    def print_items(self):
        for suitcase in self.suitcases:
            for item in suitcase.items:
                print(item)
    
    def __str__(self):
        suitcase = "suitcase" if len(self.suitcases) == 1 else "suitcases"
        return f"{len(self.suitcases)} {suitcase}, space for {self._max_weight - self.weight()} kg"


if __name__ == "__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()
