"""Defines class responsible for customers' table in database."""
import sqlite3


class CustomersDatabase:
    """This class operates on a table 'customers' in database."""

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.c = self.conn.cursor()
        self.c.execute(("""CREATE TABLE IF NOT EXISTS customers (
                        customer_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                        name TEXT,
                        lastname TEXT,
                        email TEXT,
                        access_key INTEGER NOT NULL,
                        permission INTEGER NOT NULL DEFAULT 1,
                        phone TEXT
                            
                        )"""))
        self.conn.commit()

    def fetch(self):
        """Returns all customers."""
        self.c.execute("SELECT * FROM customers")
        rows = self.c.fetchall()
        return rows

    def insert(self, name, lastname, email, access_key, phone):
        """Inserts customer to a database."""
        self.c.execute("INSERT INTO customers (name,lastname,email,access_key,phone)"
                       " VALUES (?,?,?,?,?)",
                       (name, lastname, email, access_key, phone))
        self.conn.commit()

    def remove(self, id):
        """Deletes customer from a database."""
        self.c.execute("DELETE FROM customers WHERE customer_id=?", (id,))
        self.conn.commit()

    def update(self, id, name, lastname, email, access_key, phone):
        """Updates chosen customer."""
        self.c.execute("UPDATE customers SET name=?, lastname=?,email=?,"
                       " access_key=?,phone=? WHERE customer_id=?",
                       (name, lastname, email, access_key, phone, id))
        self.conn.commit()

    def search(self, name='', lastname='', email='', access_key='', phone=''):
        """Returns customers that meet the criteria."""
        self.c.execute(
            "SELECT * FROM customers WHERE name=? OR lastname=? OR email=?"
            " OR access_key=? OR phone=? AND permission=1",
            (name.capitalize(), lastname.capitalize(), email, access_key, phone))
        rows = self.c.fetchall()
        return rows

    def search_email(self, email=''):
        """Returns customers with given email."""
        self.c.execute("SELECT * FROM customers WHERE email=?", (email,))
        rows = self.c.fetchall()
        return rows

    def search_user(self, email='', access_key=''):
        """Returns customers with given email and access key."""
        self.c.execute("SELECT * FROM customers WHERE email=? AND"
                       " access_key=?", (email, access_key))
        rows = self.c.fetchall()
        return rows

    def is_admin(self, email='', access_key=''):
        """Returns users that meet given criteria."""
        self.c.execute("SELECT * FROM customers WHERE email=? AND"
                       " access_key=? AND permission=0", (email, access_key))
        rows = self.c.fetchall()
        return rows

    def get_id(self, email='', access_key=''):
        """Returns id of logged customer."""
        self.c.execute("SELECT customer_id FROM customers WHERE"
                       " email=? AND access_key=?", (email, access_key))
        foundId = self.c.fetchone()
        return foundId[0]

    def user_data(self, id):
        """Returns data of logged user."""
        self.c.execute("SELECT * FROM customers WHERE customer_id=?", (id,))
        row = self.c.fetchone()
        return row

    def __del__(self):
        """Closes connection."""
        self.conn.close()
