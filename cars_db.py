"""Defines class responsible for cars' table in database."""
import sqlite3


class CarsDatabase:
    """This class operates on a table 'cars' in database."""

    def __init__(self, db):
        """Inits CarsDatabase."""
        self.conn = sqlite3.connect(db)
        self.c_cursor = self.conn.cursor()
        self.c_cursor.execute("""CREATE TABLE IF NOT EXISTS cars (
                        car_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                        brand TEXT,
                        model TEXT,
                        color TEXT,
                        year INTEGER,
                        instock INTEGER NOT NULL DEFAULT 1,
                            price REAL 
                        )""")
        self.conn.commit()

    def fetch(self):
        """Displays all cars in database."""
        self.c_cursor.execute("SELECT car_id, brand, model, color, year, instock, price FROM cars")
        return self.c_cursor.fetchall()

    def fetch_available(self):
        """Displays all cars that are not booked by anybody."""
        self.c_cursor.execute(
            "SELECT car_id, brand, model, color, year, instock, price FROM cars WHERE instock=1")
        return self.c_cursor.fetchall()

    def insert(self, brand, model, color, year, price):
        """Inserts car to a database."""
        self.c_cursor.execute("INSERT INTO cars (brand,model,color,year,price) VALUES (?,?,?,?,?)",
                              (brand, model, color, year, price))
        self.conn.commit()

    def remove(self, id_car):
        """Deletes car from a database."""
        self.c_cursor.execute("DELETE FROM cars WHERE car_id=?", (id_car,))
        self.conn.commit()

    def update(self, id_car, brand, model, color, year, price):
        """Updates chosen car."""
        self.c_cursor.execute(
            "UPDATE cars SET brand=?, model=?,color=?,year=?,price=? WHERE car_id=?",
            (brand, model, color, year, price, id_car))
        self.conn.commit()

    def outofstock(self, id_car):
        """Sets status of chosen car to 0."""
        self.c_cursor.execute("UPDATE cars SET instock=0 WHERE car_id=?", (id_car,))
        self.conn.commit()

    def isout(self, id_car):
        """Returns the column 'instock' of chosen car."""
        self.c_cursor.execute("SELECT instock FROM cars WHERE car_id=?", (id_car,))
        return self.c_cursor.fetchone()

    def search(self, year, price, brand='', model='', color=''):
        """Returns cars that meet the criteria."""
        self.c_cursor.execute(
            "SELECT car_id, brand, model, color, year, instock, price FROM cars WHERE brand=? OR"
            " model=? OR color=? OR year=? OR price=?",
            (brand.capitalize(), model.capitalize(), color.capitalize(), year, price))
        return self.c_cursor.fetchall()

    def search_available(self, year, price, brand='', model='', color=''):
        """Returns cars that meet the criteria."""
        self.c_cursor.execute(
            "SELECT car_id, brand, model, color, year, instock, price FROM cars WHERE (brand=? OR"
            " model=? OR color=? OR year=? OR price=?) AND (instock=1)",
            (brand.capitalize(), model.capitalize(), color.capitalize(), year, price))
        return self.c_cursor.fetchall()
