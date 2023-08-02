class Movie:
    def __init__(self, title, year, genres):
        self.title = title
        self.year = year
        self.genres = genres

def sort_movies_by_year(movies):
    sorted_movies = sorted(movies, key=lambda movie: movie.year, reverse=True)
    return sorted_movies

def sort_movies_alphabetically(movies):
    def get_sort_key(movie):
        # Remove leading "A", "An", or "The" from the title
        title = movie.title
        if title.startswith("A "):
            title = title[2:]
        elif title.startswith("An "):
            title = title[3:]
        elif title.startswith("The "):
            title = title[4:]
        return title

    sorted_movies = sorted(movies, key=get_sort_key)
    return sorted_movies

