import sqlite3

class CarsDatabase:
    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.c=self.conn.cursor()
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
        self.c.execute("SELECT * FROM cars")
        rows=self.c.fetchall()
        return rows

    def fetch_available(self):
        self.c.execute("SELECT * FROM cars WHERE instock=1")
        rows = self.c.fetchall()
        return rows

    def insert(self,brand,model,color,year,price):
        self.c.execute("INSERT INTO cars (brand,model,color,year,price) VALUES (?,?,?,?,?)",(brand,model,color,year,price))
        self.conn.commit()
    def remove(self,id):
        self.c.execute("DELETE FROM cars WHERE car_id=?",(id,))
        self.conn.commit()

    def update(self,id,brand,model,color,year,price):
        self.c.execute("UPDATE cars SET brand=?, model=?,color=?,year=?,price=? WHERE car_id=?",(brand,model,color,year,price,id))
        self.conn.commit()

    def outofstock(self,id):
        self.c.execute("UPDATE cars SET instock=0 WHERE car_id=?",(id,))
        self.conn.commit()

    def isout(self,id):
        self.c.execute("SELECT instock FROM cars WHERE car_id=?",(id,))
        row=self.c.fetchone()
        return row
        
        
    def search(self,year,price,brand='',model='',color=''):
        self.c.execute("SELECT * FROM cars WHERE brand=? OR model=? OR color=? OR year=? OR price=?",(brand.capitalize(),model.capitalize(),color.capitalize(),year,price))
        rows=self.c.fetchall()
        return rows

    def __del__(self):
        self.conn.close()

# db=CarsDatabase('mydatavase.db')
# db.insert("Nissan","Almera","blue","2005","15000")
# db.insert("Bissan","Almera","blue","2005","15000")
# db.insert("Dissan","Almera","blue","2005","15000")
# db.insert("Rissan","Almera","blue","2005","15000")




