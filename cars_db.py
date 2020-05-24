"""Defines class responsible for cars' table in database."""
import sqlite3


class CarsDatabase:
    """This class operates on a table 'cars' in database."""

    def __init__(self, db):
        """Inits CarsDatabase."""
        self.conn = sqlite3.connect(db)
        self.c = self.conn.cursor()
        self.c.execute(("""CREATE TABLE IF NOT EXISTS cars (
                        car_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                        brand TEXT,
                        model TEXT,
                        color TEXT,
                        year INTEGER,
                        instock INTEGER NOT NULL DEFAULT 1,
                            price REAL 
                        )"""))
        self.conn.commit()

    def fetch(self):
        """Displays all cars in database."""
        self.c.execute("SELECT * FROM cars")
        rows = self.c.fetchall()
        return rows

    def fetch_available(self):
        """Displays all cars that are not booked by anybody."""
        self.c.execute("SELECT * FROM cars WHERE instock=1")
        rows = self.c.fetchall()
        return rows

    def insert(self, brand, model, color, year, price):
        """Inserts car to a database."""
        self.c.execute("INSERT INTO cars (brand,model,color,year,price) VALUES (?,?,?,?,?)",
                       (brand, model, color, year, price))
        self.conn.commit()

    def remove(self, id):
        """Deletes car from a database."""
        self.c.execute("DELETE FROM cars WHERE car_id=?", (id,))
        self.conn.commit()

    def update(self, id, brand, model, color, year, price):
        """Updates chosen car."""
        self.c.execute("UPDATE cars SET brand=?, model=?,color=?,year=?,price=? WHERE car_id=?",
                       (brand, model, color, year, price, id))
        self.conn.commit()

    def outofstock(self, id):
        """Sets status of chosen car to 0."""
        self.c.execute("UPDATE cars SET instock=0 WHERE car_id=?", (id,))
        self.conn.commit()

    def isout(self, id):
        """Returns the column 'instock' of chosen car."""
        self.c.execute("SELECT instock FROM cars WHERE car_id=?", (id,))
        row = self.c.fetchone()
        return row

    def search(self, year, price, brand='', model='', color=''):
        """Returns cars that meet the criteria."""
        self.c.execute("SELECT * FROM cars WHERE brand=? OR model=? OR"
                       " color=? OR year=? OR price=?",
                       (brand.capitalize(), model.capitalize(), color.capitalize(), year, price))
        rows = self.c.fetchall()
        return rows

    def __del__(self):
        """Closes connection."""
        self.conn.close()
