import sqlite3
def num_of_directors(db):

    query = """
            SELECT *
            FROM           Country
            LIMIT 1
            """

    db.execute(query) #Information is in object c

    rows = db.fetchall() #extract information

    return rows[0][1]



if __name__ == "__main__":

    conn = sqlite3.connect('data/database.sqlite')
    db = conn.cursor()

    print(num_of_directors(db))
