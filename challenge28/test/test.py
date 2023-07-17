import pytest
from Comparisons.Comparisons import Movie,sort_movies_by_year,sort_movies_alphabetically
def test_sort_movies_by_year():
    movies = [
        Movie("The Avengers", 2012, ["Action", "Adventure", "Sci-Fi"]),
        Movie("An Inception", 2010, ["Action", "Adventure", "Sci-Fi"]),
        Movie("A The Dark Knight", 2008, ["Action", "Crime", "Drama"]),
        Movie("Toy Story", 1995, ["Animation", "Adventure", "Comedy"]),
    ]
    sorted_movies = sort_movies_by_year(movies)
    assert sorted_movies == [
        Movie("The Avengers", 2012, ["Action", "Adventure", "Sci-Fi"]),
        Movie("An Inception", 2010, ["Action", "Adventure", "Sci-Fi"]),
        Movie("A The Dark Knight", 2008, ["Action", "Crime", "Drama"]),
        Movie("Toy Story", 1995, ["Animation", "Adventure", "Comedy"]),
    ]

def test_sort_movies_alphabetically():
    movies = [
        Movie("The Avengers", 2012, ["Action", "Adventure", "Sci-Fi"]),
        Movie("An Inception", 2010, ["Action", "Adventure", "Sci-Fi"]),
        Movie("A The Dark Knight", 2008, ["Action", "Crime", "Drama"]),
        Movie("Toy Story", 1995, ["Animation", "Adventure", "Comedy"]),
    ]
    sorted_movies = sort_movies_alphabetically(movies)
    assert sorted_movies == [
        Movie("An Inception", 2010, ["Action", "Adventure", "Sci-Fi"]),
        Movie("A The Dark Knight", 2008, ["Action", "Crime", "Drama"]),
        Movie("The Avengers", 2012, ["Action", "Adventure", "Sci-Fi"]),
        Movie("Toy Story", 1995, ["Animation", "Adventure", "Comedy"]),
    ]