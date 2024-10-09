import tkinter as tk
from tkinter import messagebox
from Database import Database as DB

class PriceTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Food Price Tracker")
        self.root.geometry("300x350")

        # Dummy Database instance (replace with actual import)
        #self.db = DB("food_prices.db")  # This will be your Database class later

        # Buttons
        self.add_price_button = tk.Button(root, text="Add New Price Entry", command=self.add_price)
        self.add_price_button.pack(pady=10)
        
        self.add_food_button = tk.Button(root, text="Add New Food", command=self.add_food)
        self.add_food_button.pack(pady=10)
        
        self.add_place_button = tk.Button(root, text="Add New Place", command=self.add_place)
        self.add_place_button.pack(pady=10)
        
        self.export_button = tk.Button(root, text="Export Prices to Excel", command=self.export_to_excel)
        self.export_button.pack(pady=10)
        
        self.exit_button = tk.Button(root, text="Exit", command=self.exit_app)
        self.exit_button.pack(pady=10)

    # Dummy functions to replace with actual Database functions later
    def add_price(self):
        # Replace with actual functionality
        print("Add new price entry called")
        # self.db.add_price(...)

    def add_food(self):
        # Replace with actual functionality
        print("Add new food called")
        # self.db.add_food(...)

    def add_place(self):
        # Replace with actual functionality
        print("Add new place called")
        # self.db.add_place(...)

    def export_to_excel(self):
        # Replace with actual functionality
        print("Export to Excel called")
        # self.db.export_to_excel(...)

    def exit_app(self):
        # Confirm before exiting
        if messagebox.askokcancel("Quit", "Do you really want to exit?"):
            self.root.quit()

# Main Application Code
if __name__ == "__main__":
    root = tk.Tk()
    app = PriceTrackerApp(root)
    root.mainloop()
