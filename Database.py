import sqlite3
from datetime import datetime
import pandas as pd  # You need to install pandas for exporting to Excel
from tkinter import filedialog  # Import filedialog for file-saving dialog

class Database:
    def __init__(self, db_name="food_prices.db"):
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()
        self.make_tables()

    def make_tables(self):
        # Create FoodItems table
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS FoodItems (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                food_name TEXT NOT NULL
            );
        ''')
        
        # Create Places table
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS Places (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                place_name TEXT NOT NULL
            );
        ''')

        # Create Units table
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS Units (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                unit_name TEXT NOT NULL
            );
        ''')
        # Create Prices table
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS Prices (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                food_id INTEGER NOT NULL,
                place_id INTEGER NOT NULL,
                price REAL NOT NULL,
                amount REAL NOT NULL,
                unit TEXT NOT NULL,
                purchase_time DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (food_id) REFERENCES FoodItems(id),
                FOREIGN KEY (place_id) REFERENCES Places(id)
            );
        ''')

        self.conn.commit()

    # Function to add a new price entry
    def add_price(self, food_id, place_id, price, amount,unit, purchase_time=None):
        if purchase_time is None:
            purchase_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        self.c.execute('''
            INSERT INTO Prices (food_id, place_id, price, amount,unit, purchase_time)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (food_id, place_id, price, amount, unit, purchase_time))
        self.conn.commit()
        print(f"New price entry added: food_id={food_id}, place_id={place_id}, price={price}, amount={amount}, unit={unit}, time={purchase_time}")

    # Function to add a new food item
    def add_food(self, food_name):
        self.c.execute('''
            INSERT INTO FoodItems (food_name)
            VALUES (?)
        ''', (food_name))
        self.conn.commit()
        print(f"New food item added: {food_name}")

    # Function to add a new place
    def add_place(self, place_name):
        self.c.execute('''
            INSERT INTO Places (place_name)
            VALUES (?)
        ''', (place_name,))
        self.conn.commit()
        print(f"New place added: {place_name}")
     # Function to add a new place
    def add_unit(self, unit_name):
        self.c.execute('''
            INSERT INTO Places (unit_name)
            VALUES (?)
        ''', (unit_name,))
        self.conn.commit()
        print(f"New unit added: {unit_name}")

    # Function to export prices to an Excel file (prompts for location)
    def export_to_excel(self):
        # Prompt the user for the file location and name
        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                                 filetypes=[("Excel files", "*.xlsx")])
        if file_path:
            # Query for data to export
            self.c.execute('''
                SELECT Prices.id, FoodItems.food_name, Places.place_name, Prices.price, Prices.amount, Prices.purchase_time 
                FROM Prices
                JOIN FoodItems ON Prices.food_id = FoodItems.id
                JOIN Places ON Prices.place_id = Places.id
            ''')
            
            rows = self.c.fetchall()

            # Create a DataFrame and export to the selected Excel file
            df = pd.DataFrame(rows, columns=['ID', 'Food', 'Place', 'Price', 'Amount', 'Time'])
            df.to_excel(file_path, index=False)
            print(f"Prices exported to {file_path}")

    def close(self):
        self.conn.close()

    def get_food_names(self):
        foods = self.c.execute("SELECT food_name FROM FoodItems").fetchall()
        return [food[0] for food in foods]

    def get_place_names(self):
        places = self.c.execute("SELECT place_name FROM Places").fetchall()
        return [place[0] for place in places]
    def get_unit_names(self):
        units = self.c.execute("SELECT unit_name FROM Units").fetchall()
        return [unit[0] for unit in units]
