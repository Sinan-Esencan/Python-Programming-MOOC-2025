# The method tick adds one second to the stopwatch. The maximum value for both seconds and minutes is 59. Your class definition should also
# contain a __str__ method, which returns a string representation of the state of the stopwatch, as shown in the example above.
# Hint: it might make it easier to test the tick method if you temporarily set the initial values of the seconds and minutes to some value
# closer to 59 in the constructor. If you do change the initial values, remember to change them back before submitting.

# Write your solution here:
class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def tick(self): #add 1 second
        self.seconds += 1

        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1

        if self.minutes == 60:
            self.minutes = 0    

    def __str__(self):
        minutes = ""
        if self.minutes < 10:
            minutes = str(0) + str(self.minutes)
        else:
            minutes = str(self.minutes)

        seconds = ""
        if self.seconds < 10:
            seconds = str(0) + str(self.seconds)
        else:
            seconds = str(self.seconds)
        return f"{minutes}:{seconds}"

if __name__ == "__main__":
    watch = Stopwatch()
    for i in range(3600):
        print(watch)
        watch.tick()


# alt - mooc.fi: f-string ile cok daha pratik:
class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0
 
    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
            if self.minutes == 60:
                self.minutes = 0
 
    def __str__(self):
        return f"{self.minutes:0>2}:{self.seconds:0>2}"
# self.minutes:02 olarak da yazılabilirdi bos hucreler 0 ile dolduruldugundan dolayı
