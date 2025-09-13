# Please write a function named find_movies(database: list, search_term: str), which processes the movie database created in the previous exercise.
# The function should formulate a new list, which contains only the movies whose title includes the word searched for. Capitalisation is irrelevant
# here. A search for ana should return a list containing both Anaconda and Management

def find_movies(database: list, search_term: str):
    database_with_specific_name = []
    for movie in database:
# The function lower() converts a string to lowercase. when this is done for both strings search is case insensitive
        if search_term.lower() in movie["name"].lower():
            database_with_specific_name.append(movie)
    return database_with_specific_name

def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    dict = {"name" : name, "director" : director, "runtime" : runtime, "year" : year}
    database.append(dict)

if __name__ == "__main__":
    # database = []
    # add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
    # add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
    # print(database)

    database = [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
    {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
    {"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}]
    my_movies = find_movies(database, "python")
    print(my_movies)
    print(database)
