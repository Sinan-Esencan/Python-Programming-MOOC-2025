# soru icin: advanced course in programming > part 10 > Object oriented programming techniques > Money

class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __eq__(self, another):
        return self.__euros == another.__euros and self.__cents == another.__cents

    def __lt__(self, another):
        if self.__euros < another.__euros or self.__euros == another.__euros and self.__cents < another.__cents:
            return True
        return False
        # alt: return self.__euros < another.__euros or self.__euros == another.__euros and self.__cents < another.__cents

    def __gt__(self, another):
# *__lt__() metodundaki yapı asagıdakinin kısaltılmıs hali:*
        if self.__euros > another.__euros:
            return True
        elif self.__euros == another.__euros and self.__cents > another.__cents:
            return True
        return False

    def __ne__(self, another):
        return self.__euros != another.__euros or self.__cents != another.__cents

    def __add__(self, another):
        euros = self.__euros + another.__euros
        cents = self.__cents + another.__cents

        if cents >= 100:
            cents -= 100
            euros += 1

        return self.__class__(euros, cents)

    def __sub__(self, another):
        euros = self.__euros - another.__euros
        cents = self.__cents - another.__cents
        
        if euros < 0 or euros == 0 and cents < 0:
            raise ValueError("a negative result is not allowed")

        if euros > 0 and cents < 0:
            euros -= 1
            cents += 100

        return self.__class__(euros, cents)

    def __str__(self):        
        cents = "0"+str(self.__cents) if self.__cents < 10 else self.__cents
        # alt: "0"+str(self.__cents) yerine f"0{self.__cents}" yazılabilirdi
        return f"{self.__euros}.{cents} eur"
        
        # klasik yontem:
        # if self.__cents < 10:
        #     return f"{self.__euros}.0{self.__cents} eur"
        # else:
        #     return f"{self.__euros}.{self.__cents} eur"



# alt: mooc.fi'nin daha iyi yontemi:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents
 
    def __str__(self):
        # f-string has a handy feature for adding leading zeros:
        # :02d for example means, that output has at least 2 digit
        return f"{self.__euros}.{self.__cents:02d} eur"
 
    # Helper method for returning the value in cents
    # --> makes the comparisons easier
    def __value(self):
        return self.__euros * 100 + self.__cents
 
    # Another helper method which converts cents to value
    def __set_value(self, cents: int):
        self.__euros = cents // 100
        self.__cents = cents - self.__euros * 100
 
    def __eq__(self, other: "Money"):
        return self.__value() == other.__value()
 
    def __lt__(self, other: "Money"):
        return self.__value() < other.__value()
 
    def __gt__(self, other: "Money"):
        return self.__value() > other.__value()
 
    def __ne__(self, other: "Money"):
        return self.__value() != other.__value()
 
    def __add__(self, other: "Money"):
        msum = Money(0,0)
        msum.__set_value(self.__value() + other.__value())
        return msum
 
    def __sub__(self, other: "Money"):
        difference = self.__value() - other.__value()
        if difference < 0:
            raise ValueError("a negative result is not allowed")
        dmoney = Money(0,0)
        dmoney.__set_value(self.__value() - other.__value())
        return dmoney
