# Please define a new class named Clock which expands on the capabilities of your Stopwatch class. It should work as follows:

# clock = Clock(23, 59, 55)
# print(clock)
# clock.tick()
# print(clock)
# clock.tick()
# print(clock)
# clock.tick()
# print(clock)
# clock.tick()
# print(clock)
# clock.tick()
# print(clock)
# clock.tick()
# print(clock)
# clock.set(12, 5)
# print(clock)

# Sample output
# 23:59:55
# 23:59:56
# 23:59:57
# 23:59:58
# 23:59:59
# 00:00:00
# 00:00:01
# 12:05:00

# Write your solution here:
class Clock:
    def __init__(self,hours,minutes,seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set(self,hours,minutes):
        self.hours = hours
        self.minutes = minutes
        self.seconds = 0        

    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1

            if self.minutes == 60:
                self.minutes = 0
                self.hours += 1

                if self.hours == 24:
                    self.hours = 0

    def __str__(self):
        # return f"{self.hours}:{self.minutes}:{self.seconds}"
        return f"{self.hours:0>2}:{self.minutes:0>2}:{self.seconds:0>2}"
    


if __name__ == "__main__":
    clock = Clock(23, 59, 55)
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)

    clock.set(12, 5)
    print(clock)
