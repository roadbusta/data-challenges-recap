# pylint:disable=C0111,C0103
import sqlite3


def detailed_orders(db):
    '''return a list of all orders (order_id, customer.contact_name,
    employee.firstname) ordered by order_id'''

    query = """
            SELECT o.OrderID AS order_id,
	               c.ContactName  AS name,
	               e.FirstName AS employee
              FROM orders AS o
         LEFT JOIN Customers AS c ON o.CustomerID = c.CustomerID
         LEFT JOIN Employees AS e ON o.EmployeeID = e.EmployeeID
          ORDER BY 1 ASC
            """

    db.execute(query)

    return db.fetchall()

def spent_per_customer(db):
    '''return the total amount spent per customer ordered by ascending total
    amount (to 2 decimal places)
    Exemple :
        Jean   |   100
        Marc   |   110
        Simon  |   432
        ...
    '''
    pass  # YOUR CODE HERE

def best_employee(db):
    '''Implement the best_employee method to determine who’s the best employee! By “best employee”, we mean the one who sells the most.
    We expect the function to return a tuple like: ('FirstName', 'LastName', 6000 (the sum of all purchase)). The order of the information is irrelevant'''
    pass  # YOUR CODE HERE

def orders_per_customer(db):
    '''TO DO: return a list of tuples where each tupe contains the contactName
    of the customer and the number of orders they made (contactName,
    number_of_orders). Order the list by ascending number of orders'''
    pass  # YOUR CODE HERE

if __name__ == "__main__":
    conn = sqlite3.connect("data/ecommerce.sqlite")

    db = conn.cursor()

    print(detailed_orders(db))
