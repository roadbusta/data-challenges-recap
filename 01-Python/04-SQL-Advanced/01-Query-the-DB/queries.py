# pylint:disable=C0111,C0103
import sqlite3

def query_orders(db):
    # return a list of orders displaying each column
    query = """
            SELECT *
            FROM orders
            """

    db.execute(query)


    return db.fetchall()

def get_orders_range(db, date_from, date_to):
    # return a list of orders displaying all columns with OrderDate between
    # date_from and date_to (excluding date_from and including date_to)
    query = """
            SELECT *
            FROM orders
            WHERE DATE(OrderDate) >  DATE(?)
            AND DATE(OrderDate) <= DATE(?)
            ORDER BY OrderDate ASC
            """
    db.execute(query, (f"{date_from}", f"{date_to}"))

    return db.fetchall()

def get_waiting_time(db):
    # get a list with all the orders displaying each column
    # and calculate an extra TimeDelta column displaying the number of days
    # between OrderDate and ShippedDate, ordered by ascending TimeDelta

    query = """
            SELECT *,
	        JULIANDAY(ShippedDate) - JULIANDAY(OrderDate) AS TimeDelta
            FROM orders
            ORDER BY TimeDelta ASC
            """
    db.execute(query)

    return db.fetchall()

# if __name__ == "__main__":
    # con = sqlite3.connect("data/ecommerce.sqlite")

    # db = con.cursor()
    # date_from = '2012-01-04'
    # date_to = '2012-01-31'

    # print(get_orders_range(db, date_from, date_to))
