# pylint: disable=missing-docstring, C0103
import sqlite3


def directors_count(db):
    # return the number of directors contained in the database
    query = """
               SELECT COUNT(*)
               FROM directors
               """

    db.execute(query)
    return db.fetchone()[0]


def directors_list(db):
    # return the list of all the directors sorted in alphabetical order
    query = """
               SELECT name
               FROM directors
               ORDER BY name ASC
               """

    db.execute(query)

    #Use list comprehension to build a list
    director_list = [ row["name"] for row in db.fetchall()]
    return director_list


def love_movies(db):
    # return the list of all movies which contain the exact word "love"
    # in their title, sorted in alphabetical order
    query = """
               SELECT title
                FROM movies
                WHERE UPPER(title) LIKE "%LOVE%"
                ORDER BY title ASC
               """

    db.execute(query)

    #Use list comprehension to build a list
    love_movies = [row["title"] for row in db.fetchall()]
    return love_movies


def directors_named_like_count(db, name):
    # return the number of directors which contain a given word in their name

    query = """
               SELECT COUNT(name)
               FROM directors
               WHERE UPPER(name) LIKE ?
               """

    db.execute(query, (f"%{name}%",))

    return db.fetchone()[0]


def movies_longer_than(db, min_length):
    # return this list of all movies which are longer than a given duration,
    # sorted in the alphabetical order

    query = """
            SELECT title
            FROM movies
            WHERE minutes > ?
            ORDER BY title ASC
            """
    db.execute(query, (min_length,))

    #Use list comprehension to build a list
    movies_list = [row["title"] for row in db.fetchall()]


    return movies_list

if __name__ == "__main__":

    # Initiate connection
    conn = sqlite3.connect("data/movies.sqlite")

    # Question 1
    #Create cursor
    db = conn.cursor()
    print("Number of directors: ", directors_count(db))

    # # Question 2
    # conn.row_factory = sqlite3.Row
    # db = conn.cursor()
    # print(directors_list(db))

    # # Question 3
    # conn.row_factory = sqlite3.Row
    # db = conn.cursor()
    # print(love_movies(db))

    # # Question 4
    # #Create cursor
    # db = conn.cursor()
    # name = "son"
    # print(f"Number of directors with name containing {name}: ", directors_named_like_count(db, name))

    # # Question 5
    # conn.row_factory = sqlite3.Row
    # db = conn.cursor()
    # min = 300
    # print(movies_longer_than(db,min))
