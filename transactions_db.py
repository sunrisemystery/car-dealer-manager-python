"""Defines class responsible for transactions' table in database."""
import sqlite3
import cars_db
import customers_db


class TransactionsDatabase(cars_db.CarsDatabase, customers_db.CustomersDatabase):
    """This class operates on a table 'transactions' in database."""

    def __init__(self, db):
        """Inits TransactionsDatabase."""
        self.conn = sqlite3.connect(db)
        self.c = self.conn.cursor()
        self.c.execute(("""CREATE TABLE IF NOT EXISTS transactions (
                transaction_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                customer_id INTEGER NOT NULL,
                car_id INTEGER NOT NULL,
                date DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
                FOREIGN KEY (car_id) REFERENCES cars(car_id)
               
                )"""))
        self.conn.commit()

    def insert_transaction(self, customer_id, car_id):
        """Inserts transaction to a database."""
        self.c.execute("INSERT INTO transactions (customer_id, car_id)"
                       " VALUES (?,?)", (customer_id, car_id))
        self.conn.commit()

    def search_transactions(self, customer_id):
        """Returns transactions that meet the criteria."""
        self.c.execute('''SELECT transactions.transaction_id, cars.brand,
         cars.model,cars.color,cars.year,cars.price, transactions.date 
        FROM transactions 
        INNER JOIN cars 
        ON transactions.car_id=cars.car_id 
        WHERE transactions.customer_id=? '''
                       , (customer_id,))
        rows = self.c.fetchall()
        return rows

    def all_transactions(self):
        """Returns all transactions."""
        self.c.execute('''SELECT transactions.transaction_id,customers.name,
        customers.lastname, cars.brand, cars.model,cars.color,cars.year,cars.price, transactions.date 
                FROM transactions 
                INNER JOIN cars 
                ON transactions.car_id=cars.car_id
                INNER JOIN customers
                ON transactions.customer_id=customers.customer_id 
                ''')

        rows = self.c.fetchall()
        return rows

    def remove(self, id):
        """Deletes transaction from a database."""
        self.c.execute("SELECT car_id FROM transactions WHERE transaction_id=?", (id,))
        found_car_id = self.c.fetchone()
        self.c.execute("UPDATE cars SET instock=1 WHERE car_id=?",
                       (found_car_id[0],))
        self.conn.commit()
        self.c.execute("DELETE FROM transactions WHERE transaction_id=?", (id,))
        self.conn.commit()

    def __del__(self):
        """Closes connection."""
        self.conn.close()
