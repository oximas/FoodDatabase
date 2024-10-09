import tkinter as tk
from tkinter import messagebox
from Database import Database as DB

class PriceTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Food Price Tracker")
        self.root.geometry("300x350")

        # Dummy Database instance (replace with actual import)
        self.db = DB("food_prices.db")  # This will be your Database class later

        # Buttons
        self.add_price_button = tk.Button(root, text="Add New Price Entry", command=self.price_adding_page)
        self.add_price_button.pack(pady=10)
        
        self.add_food_button = tk.Button(root, text="Add New Food", command=self.food_adding_page)
        self.add_food_button.pack(pady=10)
        
        self.add_place_button = tk.Button(root, text="Add New Place", command=self.place_adding_page)
        self.add_place_button.pack(pady=10)
        
        self.export_button = tk.Button(root, text="Export Prices to Excel", command=self.export_to_excel)
        self.export_button.pack(pady=10)
        
        self.exit_button = tk.Button(root, text="Exit", command=self.exit_app)
        self.exit_button.pack(pady=10)

    def price_adding_page(self):
        # Clear the current widgets
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Add a label for price entry
        tk.Label(self.root, text="Add New Price Entry", font=("Arial", 16)).pack(pady=10)

        # Entry for food ID
        tk.Label(self.root, text="Food ID:").pack(pady=5)
        food_id_entry = tk.Entry(self.root)
        food_id_entry.pack(pady=5)

        # Entry for place ID
        tk.Label(self.root, text="Place ID:").pack(pady=5)
        place_id_entry = tk.Entry(self.root)
        place_id_entry.pack(pady=5)

        # Entry for price
        tk.Label(self.root, text="Price:").pack(pady=5)
        price_entry = tk.Entry(self.root)
        price_entry.pack(pady=5)

        # Entry for amount
        tk.Label(self.root, text="Amount:").pack(pady=5)
        amount_entry = tk.Entry(self.root)
        amount_entry.pack(pady=5)

        # Button to submit the price entry
        tk.Button(self.root, text="Submit", command=lambda: self.submit_price(food_id_entry.get(), place_id_entry.get(), price_entry.get(), amount_entry.get())).pack(pady=10)

        # Button to go back to the main menu
        tk.Button(self.root, text="Back", command=self.main_menu).pack(pady=5)

    def food_adding_page(self):
        # Clear the current widgets
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Add a label for food entry
        tk.Label(self.root, text="Add New Food Item", font=("Arial", 16)).pack(pady=10)

        # Entry for food name
        tk.Label(self.root, text="Food Name:").pack(pady=5)
        food_name_entry = tk.Entry(self.root)
        food_name_entry.pack(pady=5)

        # Entry for unit
        tk.Label(self.root, text="Unit:").pack(pady=5)
        unit_entry = tk.Entry(self.root)
        unit_entry.pack(pady=5)

        # Button to submit the food entry
        tk.Button(self.root, text="Submit", command=lambda: self.submit_food(food_name_entry.get(), unit_entry.get())).pack(pady=10)

        # Button to go back to the main menu
        tk.Button(self.root, text="Back", command=self.main_menu).pack(pady=5)

    def place_adding_page(self):
        # Clear the current widgets
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Add a label for place entry
        tk.Label(self.root, text="Add New Place", font=("Arial", 16)).pack(pady=10)

        # Entry for place name
        tk.Label(self.root, text="Place Name:").pack(pady=5)
        place_name_entry = tk.Entry(self.root)
        place_name_entry.pack(pady=5)

        # Button to submit the place entry
        tk.Button(self.root, text="Submit", command=lambda: self.submit_place(place_name_entry.get())).pack(pady=10)

        # Button to go back to the main menu
        tk.Button(self.root, text="Back", command=self.main_menu).pack(pady=5)

    def main_menu(self):
        # Clear the current widgets
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Main menu buttons
        self.add_price_button = tk.Button(self.root, text="Add New Price Entry", command=self.price_adding_page)
        self.add_price_button.pack(pady=10)

        self.add_food_button = tk.Button(self.root, text="Add New Food", command=self.food_adding_page)
        self.add_food_button.pack(pady=10)

        self.add_place_button = tk.Button(self.root, text="Add New Place", command=self.place_adding_page)
        self.add_place_button.pack(pady=10)

        self.export_button = tk.Button(self.root, text="Export Prices to Excel", command=self.export_to_excel)
        self.export_button.pack(pady=10)

        self.exit_button = tk.Button(self.root, text="Exit", command=self.exit_app)
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
