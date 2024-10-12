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
        self.root.geometry("300x500")

        # Entry for food ID
        tk.Label(self.root, text="Add New Price Entry", font=("Arial", 16)).pack(pady=10)

        # Fetch food items from the database
       
        food_names = self.db.get_food_names()  # Extract food names

        # Create a dropdown for food selection
        tk.Label(self.root, text="Select Food:").pack(pady=5)
        food_var = tk.StringVar(self.root)
        def__food_value = food_names[0] if food_names else "No food items available"
        food_var.set(def__food_value)  # Default value
        food_menu = tk.OptionMenu(self.root, food_var,def__food_value, *food_names)
        food_menu.pack(pady=5)

        # Fetch places from the database
        place_names = self.db.get_place_names()  # Extract place names

        # Create a dropdown for place selection
        tk.Label(self.root, text="Select Place:").pack(pady=5)
        place_var = tk.StringVar(self.root)
        def_place_value = place_names[0] if place_names else "No places available"
        place_var.set(def_place_value)  # Default value
        place_menu = tk.OptionMenu(self.root, place_var,def_place_value, *place_names)
        place_menu.pack(pady=5)

        # Entry for price
        tk.Label(self.root, text="Price:").pack(pady=5)
        price_entry = tk.Entry(self.root)
        price_entry.pack(pady=5)

        # Entry for amount
        tk.Label(self.root, text="Amount:").pack(pady=5)
        amount_entry = tk.Entry(self.root)
        amount_entry.pack(pady=5)

         # Fetch places from the database
        unit_names = self.db.get_unit_names()  # Extract place names

        # Create a dropdown for unit selection
        tk.Label(self.root, text="Select Unit:").pack(pady=5)
        unit_var = tk.StringVar(self.root)
        def_unit_value = unit_names[0] if unit_names else "No units available"
        unit_var.set(def_unit_value)  # Default value
        unit_menu = tk.OptionMenu(self.root, unit_var,def_unit_value, *unit_names)
        unit_menu.pack(pady=5)

        # Button to submit the price entry
        food_value = food_var.get()
        place_value = place_var.get()
        price_value = price_entry.get()
        amount_value = amount_entry.get()
        unit_value = unit_var.get()
        tk.Button(self.root, text="Submit", command=lambda: self.add_price(food_value, place_value, price_value, amount_value,unit_value)).pack(pady=10)
        #if(food_value and price_value and amount_value and place_value and unit_value):
        #else:
        #    messagebox.showwarning("all entries should be filled")
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

        # Button to submit the food entry
        tk.Button(self.root, text="Submit", command=lambda: self.add_food(food_name_entry.get())).pack(pady=10)

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
        tk.Button(self.root, text="Submit", command=lambda: self.add_place(place_name_entry.get())).pack(pady=10)

        # Button to go back to the main menu
        tk.Button(self.root, text="Back", command=self.main_menu).pack(pady=5)
    def add_price(self,food, place, price, amount,unit):
        if food and place and price and amount and unit:
            self.db.add_price(food, place, price, amount,unit)
        else:
            messagebox.showwarning("All etnries should be filled")
    def add_food(self,food):
        if food:
            self.db.add_food(food)
        else:
            messagebox.showwarning("All etnries should be filled")
    def add_place(self,place):
        if place :
            self.db.add_place(place)
        else:
            messagebox.showwarning("All etnries should be filled")
        
    def main_menu(self):
        # Clear the current widgets
        for widget in self.root.winfo_children():
            widget.destroy()
        self.root.geometry("300x350")
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
