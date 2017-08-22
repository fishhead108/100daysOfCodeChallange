import csv
from collections import namedtuple
from statistics import mean
import operator

MOVIE_DATA = 'movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director(filename: str) -> dict:
    '''Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)'''
    my_movies = {}
    Data = namedtuple("Data", ('movie_title', 'title_year', 'imdb_score'))

    with open(filename, 'rt', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            if row['director_name'] not in my_movies:
                my_movies[row['director_name']] = [
                    Data((row['movie_title']).strip(), row['title_year'], row['imdb_score'])]
            else:
                my_movies[row['director_name']] += [
                    Data((row['movie_title']).strip(), row['title_year'], row['imdb_score'])]
    return my_movies


def get_average_scores(directors: dict):
    '''Filter directors with < MIN_MOVIES and calculate averge score'''
    new_directors = {}
    for director, movies in directors.items():
        if len(movies) >= MIN_MOVIES:
            avg_score = round(_calc_mean(movies), 1)
            new_directors[director] = sorted(movies, key=lambda movie: movie.imdb_score, reverse=True), avg_score

    return new_directors


def _calc_mean(movies):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    return mean([float(movie.imdb_score) for movie in movies])


def print_results(directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''

    _sorter_by_avg = sorted(directors, key=lambda director: directors[director][-1], reverse=True)

    for index, director in enumerate(_sorter_by_avg, 1):
        print(f'\n{index}. {director:<51} {directors[director][-1]}')
        print('-' * 60)
        for movie in directors[director][0]:
            if not isinstance(movie, float):
                print(f'{movie.title_year}] {movie.movie_title:<50} {movie.imdb_score}')


def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    directors = get_movies_by_director(MOVIE_DATA)
    directors = get_average_scores(directors)
    print_results(directors)


if __name__ == '__main__':
    main()
