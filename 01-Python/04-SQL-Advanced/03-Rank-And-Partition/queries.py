# pylint:disable=C0111,C0103
import sqlite3
def order_rank_per_customer(db):
    query = """
            SELECT OrderID,
                   CustomerID,
                   OrderDate,
                   RANK()  OVER(
       				           PARTITION BY CustomerID
       				               ORDER BY OrderDate
                               ) AS OrderRank
            FROM Orders
            ORDER BY OrderDate ASC
            """

    db.execute(query)

    return db.fetchall()


def order_cumulative_amount_per_customer(db):
    query = """
            SELECT o.OrderID AS OrderID,
                   o.CustomerID AS CustomerID,
                   o.OrderDate AS OrderDate,
                   ROUND(SUM(SUM(od.UnitPrice * od.Quantity)) OVER(
       				                             PARTITION BY o.CustomerID
       				                                 ORDER BY o.OrderDate
                                                            ),1) AS OrderCumulativeAmount
                    FROM Orders o
            JOIN OrderDetails od ON o.OrderId = od.OrderID
            GROUP BY od.OrderID
            ORDER BY o.CustomerID  ASC
            """
    db.execute(query)
    return db.fetchall()

if __name__ == "__main__":
    conn = sqlite3.connect('data/ecommerce.sqlite')

    db = conn.cursor()

    print(order_cumulative_amount_per_customer(db))
