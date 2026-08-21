# In this exercise you are asked to implement the class SimpleDate which allows you to handle dates. For simplicity's sake we assume here that each month has 30 days.
# Because of this simplification you should not use the datetime module from the Python standard library. You will implement similar functionality by yourself instead
# part 1) Comparisons
# Please implement the outline of the class, along with methods allowing for comparisons with the operators <, >, == and !=.
# part 2) Increment
# Please implement the addition operator + which allows you to add a given number of days to a SimpleDate object. The operator should return a new SimpleDate object. The original object should not be changed.
# part 3) Difference
# Please implement the subtraction operator - which allows you to find out the difference in days between two SimpleDate objects. As we assumed each month to have 30 days, a year within the confines of this exercise is 12*30 = 360 days long.

class SimpleDate:
    def __init__(self, day, months, year):
        self.day = day
        self.months= months
        self.year = year

    def __lt__(self, another):
        if self.year < another.year:
            return True

        if self.year == another.year and self.months < another.months:
            return True

        if self.year == another.year and self.months == another.months and self.day < another.day:
            return True
        
        return False

    def __gt__(self, another):
        if self.year > another.year:
            return True

        if self.year == another.year and self.months > another.months:
            return True

        if self.year == another.year and self.months == another.months and self.day > another.day:
            return True
        
        return False

    def __eq__(self, another):
        return self.year == another.year and self.months == another.months and self.day == another.day
    
    def __neq__(self, another):
        return not (self.year == another.year and self.months == another.months and self.day == another.day)

    def __add__(self, days): #zaman + sure = zaman
        # day = self.day + days
        # real_days = day % 30
        # months = self.months + day // 30
        # real_months = months % 12
        # year = self.year + months // 12
        # return self.__class__(real_days, real_months, year)

        # daha iyi version (once toplam gune cevrilir)
        time_in_days = self.day_maker()
        total_days = time_in_days + days #zaman + sure = zaman (gun bazında olmasına ragmen zaman)
        date = self.date_maker(total_days)
        return date

    def date_maker(self, total_days):
        year = total_days // 360
        remaining_time_with_months = total_days % 360
        months = remaining_time_with_months // 30
        day = remaining_time_with_months % 30
        return self.__class__(day, months, year)

    def __sub__(self, another): #zaman - zaman = sure
        #halen ikisi de zaman ancak baslangıctan itibaren gun sayıları hesaplanıyor:
        time1_in_days = self.day_maker()
        time2_in_days = another.day_maker()

        duration = time1_in_days - time2_in_days

        # if duration < 0:
        #     return -duration

        # return duration
        
        # yukarıdaki early return yerine abs() kullanmak daha mantıklı
        return abs(duration)
        
    def day_maker(self):
        return self.year * 360 + self.months * 30 + self.day

    def __str__(self):
        return f"{self.day}.{self.months}.{self.year}"


# mooc.fi versiyonu:
class SimpleDate:
    def __init__(self, pv: int, month: int, year: int):
        self.__pv = pv
        self.__month = month
        self.__year = year
 
    def __str__(self):
        return f'{self.__pv}.{self.__month}.{self.__year}'
 
    # Comparisons are easier, when date is converted to days
    def __value(self):
        return self.__year * 360 + self.__month * 30 + self.__pv
 
    # Converst days back to date
    def __to_date(self, days: int):
        months = days // 30
        years = months // 12
        days -= months * 30
        months -= years * 12
        return SimpleDate(days, months, years)
 
    def __lt__(self, other: "SimpleDate"):
        return self.__value() < other.__value()
 
    def __gt__(self, other: "SimpleDate"):
        return self.__value() > other.__value()
 
    def __eq__(self, other: "SimpleDate"):
        return self.__value() == other.__value()
        
    def __ne__(self, other: "SimpleDate"):
        return self.__value() != other.__value()
 
    def __add__(self, days_to_add: int):
        return self.__to_date(self.__value() + days_to_add)
 
    def __sub__(self, other: "SimpleDate"):
        # abs(x) returns the absolute value of x
        return abs(self.__value() - other.__value())
