# Part 1: A class named Series
# Please write a class named Series whose __str__ method prints the following:
# Dexter (8 seasons)
# genres: Crime, Drama, Mystery, Thriller
# no ratings
# The constructor should take the title, the number of seasons and a list of genres for the series as its arguments.
# Hint: whenever you need to produce a string from a list containing strings, with a separating character of your choice in between the entries, you can 
# use the join method as follows:

# Part 2: Adding reviews:
# Please implement the method rate(rating: int) which lets you add a rating between 0 and 5 to any series object. You will also need to adjust the 
# __str__ method so that in case there are ratings, the method prints out the number of ratings added, and their average rounded to one decimal point.

# Part 3: Searching for series:
# Please implement these two functions which allow you to search through a list of series: minimum_grade(rating: float, series_list: list) 
# and includes_genre(genre: str, series_list: list).

class Series:
    def __init__(self, title, number_of_seasons, list_of_genres):
        self.title = title
        self.number_of_seasons = number_of_seasons
        self.list_of_genres = list_of_genres
        self.rating = []

    def __str__(self):
        rating = "no ratings"
        if self.rating:
            rating = f"{len(self.rating)} ratings, average {(sum(self.rating)/len(self.rating)):.1f} points"
        return (f"{self.title} ({self.number_of_seasons} seasons)\n"
                f"genres: {", ".join(self.list_of_genres)}\n"
                f"{rating}")
    # alt: Triple quote:
    # return f"""{self.title} ({self.number_of_seasons} seasons)
    # genres: {', '.join(self.list_of_genres)}
    # {rating}"""

    def rate(self, rating: int):
        self.rating.append(rating)

def minimum_grade(rating: float, series_list: list):
    modified_series_list = []
    for series in series_list:
        # rating = f"{(sum(series.rating)/len(series.rating)):.1f}"
        series_rating = sum(series.rating)/len(series.rating)
        if series_rating >= rating:
            modified_series_list.append(series)
    return modified_series_list
        
        
def includes_genre(genre: str, series_list: list):
    modified_series_list = []
    for series in series_list:
        if genre in series.list_of_genres:
            modified_series_list.append(series)
    return modified_series_list

if __name__ == "__main__":
    # 1
    # dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    # print(dexter)

    # 2
    # dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    # dexter.rate(4)
    # dexter.rate(5)
    # dexter.rate(5)
    # dexter.rate(3)
    # dexter.rate(0)
    # print(dexter)

    # 3
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)
    s1.rate(3)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4:")
    for series in minimum_grade(4, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)


# alt - mooc.fi: notları listeye alma isi ilginc:
class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings = [0, 0, 0, 0, 0, 0]
        self.number_of_ratings = 0
 
    def grade(self):
        if self.number_of_ratings == 0:
            return 0
        else:
            grade_sum = 0
            for i in range(0, 6):
                grade_sum += self.ratings[i] * i
            return grade_sum / self.number_of_ratings
 
 
    def __str__(self):
        genres = ", ".join(self.genres)
 
        if self.number_of_ratings == 0:
            ratings = "no ratings"
        else:
            grade_sum = 0
            for i in range(0, 6):
                grade_sum += self.ratings[i] * i
            ka = grade_sum / self.number_of_ratings
            ratings = f"{self.number_of_ratings} ratings, average {ka:.1f} points"
 
        return f"{self.title} ({self.seasons} seasons)\ngenres: {genres}\n{ratings}"
 
    def rate(self, grade: int):
        self.number_of_ratings += 1
        self.ratings[grade] += 1
 
def minimum_grade(grade: float, seriest: list):
    result = []
    for series in seriest:
        if series.grade() >= grade:
            result.append(series)
 
    return result
 
def includes_genre(genre: str, seriest: list):
    result = []
    for series in seriest:
        if genre in series.genres:
            result.append(series)
 
    return result
 
if __name__ == "__main__":
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)
    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)
    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)
    seriest = [s1, s2, s3]
 
    answer = minimum_grade(4.5, seriest)
    print(answer)
# Write your solution here:
