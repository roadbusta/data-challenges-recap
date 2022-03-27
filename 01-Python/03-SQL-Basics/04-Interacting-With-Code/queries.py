# pylint: disable=missing-docstring, C0103
import sqlite3


def directors_count(db):
    # return the number of directors contained in the database
    db.execute("""
               SELECT COUNT(*)
               FROM directors
               """)
    return db.fetchone()[0]


def directors_list(db):
    # return the list of all the directors sorted in alphabetical order
    db.execute("""
               SELECT name
               FROM directors
               ORDER BY name ASC
               """)

    #Use list comprehension to build a list
    director_list = [ row["name"] for row in db.fetchall()]
    return director_list


def love_movies(db):
    # return the list of all movies which contain the exact word "love"
    # in their title, sorted in alphabetical order
    db.execute("""
               SELECT title
                FROM movies
                WHERE UPPER(title) LIKE "%LOVE%"
                ORDER BY title ASC
               """)

    #Use list comprehension to build a list
    love_movies = [row["title"] for row in db.fetchall()]
    return love_movies



def directors_named_like_count(db, name):
    # return the number of directors which contain a given word in their name
    pass  # YOUR CODE HERE


def movies_longer_than(db, min_length):
    # return this list of all movies which are longer than a given duration,
    # sorted in the alphabetical order
    pass  # YOUR CODE HERE

if __name__ == "__main__":

    # Initiate connection
    conn = sqlite3.connect("data/movies.sqlite")

    # # Question 1
    # #Create cursor
    # db = conn.cursor()

    # print("Number of directors: ", directors_count(db))

    # # Question 2
    # conn.row_factory = sqlite3.Row
    # db = conn.cursor()
    # print(directors_list(db))

    # # Question 3
    conn.row_factory = sqlite3.Row
    db = conn.cursor()
    print(love_movies(db))
