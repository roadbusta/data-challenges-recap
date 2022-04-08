import sqlite3

def interpolation(db,weight):

    query = """
            SELECT player_name,
	                weight
                FROM Player
                WHERE WEIGHT > ?
                AND NAME LIKE "?"
            """
    db.execute(query, (f"{weight}", ) )

    return db.fetchall()


if __name__ == "__main__":

    #Create a connection
    conn = sqlite3.connect("data/database.sqlite")

    #Create cursor
    db = conn.cursor()
    min_weight = 210

    print(interpolation(db, min_weight))
