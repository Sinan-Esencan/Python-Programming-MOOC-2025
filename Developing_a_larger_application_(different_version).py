# soru: Advanced Course in Programming > Developing a larger application
class ExerciseCounter: #sozlukte value olacak mini class
    def __init__(self):
        self.__exercises = 0

    def done(self):
        self.__exercises += 1

    def how_many(self):
        return self.__exercises


class Exercise: #logic
    def __init__(self):
        self.__students = {}

    def add_exercise(self, name):
        if name not in self.__students:
            self.__students[name] = ExerciseCounter()

        # add a new done exercise to the counter
        self.__students[name].done()
    
    def all_exercises(self):
        return self.__students


class ExerciseApplication: #UI
    def __init__(self):
        self.__exercise = Exercise()

    def printer(self):
        print()
        print("exercises completed:")
        
        for student, exercises in self.__exercise.all_exercises().items():
            print(f"{student}'s exercises: {exercises.how_many()}")
    
    def execute(self):
        print("let's do some exercises")
        while True:
            name = input("student: ")
            if len(name) == 0: #enter ile break
                self.printer()
                break
            self.__exercise.add_exercise(name)
            
app = ExerciseApplication()
app.execute()
