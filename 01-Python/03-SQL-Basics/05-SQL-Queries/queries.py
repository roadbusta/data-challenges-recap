# pylint: disable=C0103, missing-docstring
import sqlite3

def detailed_movies(db):
    '''return the list of movies with their genres and director name'''
    query = """
            SELECT m.title
            , m.genres
            , d.name
            FROM movies AS m
            LEFT JOIN directors AS d ON m.director_id = d.id
            """

    db.execute(query)
    #Use list comprehension to build a list
    detailed_movie_list = [(row["title"], row["genres"], row["name"]) for row in db.fetchall()]

    return detailed_movie_list


def late_released_movies(db):
    '''return the list of all movies released after their director death'''
    query = """
            SELECT m.title
            FROM movies AS m
            LEFT JOIN directors AS d ON m.director_id = d.id
            WHERE CAST(m.start_year AS INT) > CAST(d.death_year AS INT)
            """

    db.execute(query)

    #Use list comprehension to build a list
    late_movie_list = [row["title"]for row in db.fetchall()]

    return late_movie_list


def stats_on(db, genre_name):
    '''return a dict of stats for a given genre'''
    query = """
            SELECT genres
          , COUNT(genres) AS num
          , ROUND(AVG(minutes),2) AS len
            FROM movies
            WHERE genres = ?
            """

    db.execute(query, (f"{genre_name}",))

    results = db.fetchone()
    dictionary = { "genre" : results[0],
         "number_of_movies": results[1],
              "avg_length" : results[2] }

    return dictionary


def top_five_directors_for(db, genre_name):
    '''return the top 5 of the directors with the most movies for a given genre'''
    query = """
            SELECT d.name AS name
                 , COUNT(m.title) AS num
              FROM movies AS m
         LEFT JOIN directors  AS d ON m.director_id = d.id
             WHERE m.genres = ?
             GROUP BY d.name
          ORDER BY COUNT(m.title) DESC, d.name ASC
             LIMIT 5
            """
    db.execute(query, (f"{genre_name}", ))

    #Use list comprehension to create list of tuples
    movie_director_list = [(row["name"], row["num"]) for row in db.fetchall()]

    return movie_director_list


def movie_duration_buckets(db):
    '''return the movie counts grouped by bucket of 30 min duration'''
    query = """
            SELECT
                   (minutes/ 30 + 1 ) * 30 AS time_range
                 , COUNT(minutes) as num
              FROM movies
             WHERE time_range IS NOT NULL
          GROUP BY time_range
            """
    db.execute(query)

    return db.fetchall()


def top_five_youngest_newly_directors(db):
    '''return the top 5 youngest directors when they direct their first movie'''
    query = """
            SELECT d.name
                 , CAST(m.start_year AS INT) - CAST(d.birth_year AS INT) AS movie_age
              FROM directors AS d
         LEFT JOIN movies AS m ON m.director_id = d.id
             WHERE birth_year IS NOT NULL
          ORDER BY movie_age ASC
             LIMIT 5
            """
    db.execute(query)

    return db.fetchall()

if __name__ == "__main__":
    #Create connection
    conn = sqlite3.connect("data/movies.sqlite")

    # # Question 1
    # conn.row_factory = sqlite3.Row
    # db = conn.cursor()
    # print(detailed_movies(db))

    # # Question 2
    # conn.row_factory = sqlite3.Row
    # db = conn.cursor()
    # print(late_released_movies(db))

    # # Question 3
    # db = conn.cursor()
    # genre_name = 'Action,Adventure,Comedy'
    # print(stats_on(db, genre_name))

    # # Question 4
    # conn.row_factory = sqlite3.Row
    # db = conn.cursor()
    # genre_name = 'Action,Adventure,Comedy'
    # print(top_five_directors_for(db, genre_name))

    # # Question 5
    # db = conn.cursor()
    # print(movie_duration_buckets(db))

    # # # Question 6
    # db = conn.cursor()
    # print(top_five_youngest_newly_directors(db))
