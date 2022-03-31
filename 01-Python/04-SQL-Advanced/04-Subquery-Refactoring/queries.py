# pylint:disable=C0111,C0103
import sqlite3

def get_average_purchase(db):
    # return the average amount spent per order for each customer ordered by customer ID
    query = """
                WITH amount_per_order AS (
                            SELECT   OrderID,
                                     SUM(UnitPrice * Quantity) AS OrderTotal
                            FROM   OrderDetails
                            GROUP BY OrderID
                                        )
                SELECT o.CustomerID,
	                   ROUND(AVG(a.OrderTotal),2) AS AverageOrderedAmount
                FROM   Orders AS o
                JOIN   amount_per_order AS a ON a.OrderID = o.OrderID
                GROUP BY 1
                """
    db.execute(query)

    return db.fetchall()

def get_general_avg_order(db):
    # return the average amount spent per order
    pass  # YOUR CODE HERE

def best_customers(db):
    # return the customers who have an average purchase greater than the general average purchase
    pass  # YOUR CODE HERE

def top_ordered_product_per_customer(db):
    # return the list of the top ordered product by each customer based on the total ordered amount in USD
    pass  # YOUR CODE HERE

def average_number_of_days_between_orders(db):
    # return the average number of days between two consecutive orders of the same customer
    pass  # YOUR CODE HERE

if __name__ == "__main__":
    conn = sqlite3.connect("data/ecommerce.sqlite")

    db = conn.cursor()

    print(get_average_purchase(db))
