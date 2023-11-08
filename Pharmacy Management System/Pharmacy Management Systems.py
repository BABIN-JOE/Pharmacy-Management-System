import tkinter as tk
from tkinter import ttk
import json

"""
----------------------------------------------------------------------------------------------------
 Developed by - Babin Joe
 Github - https://github.com/BABIN-JOE/
----------------------------------------------------------------------------------------------------
"""

def main():
    root = tk.Tk()
    root.attributes('-fullscreen', True)  # Set the window to full-screen

class PharmacyManagementSystem:
    def __init__(self, data_file):
        self.medicines = {}
        self.data_file = data_file
        self.load_data()

    def add_medicine(self, name, cost, quantity, med_type, brand):
        if name in self.medicines: 
            self.medicines[name] = {
                "cost": cost,
                "quantity": quantity,
                "type": med_type,
                "brand": brand
            }
            self.save_data()

    def delete_medicine(self, name):
        if name in self.medicines:
            del self.medicines[name]
            self.save_data()

    def edit_medicine(self, name, cost, quantity, med_type, brand):
        if name in self.medicines:
            self.medicines[name] = {
                "cost": cost,
                "quantity": quantity,
                "type": med_type,
                "brand": brand
            }
            self.save_data()

    def get_inventory(self):
        inventory = "Inventory:\n"
        for name, info in self.medicines.items():
            inventory += f"Name: {name}, Cost: {info['cost']}, Quantity: {info['quantity']}, Type: {info['type']}, Brand: {info['brand']}\n"
        return inventory

    def load_data(self):
        try:
            with open(self.data_file, "r") as file:
                self.medicines = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.medicines = {}

    def save_data(self):
        with open(self.data_file, "w") as file:
            json.dump(self.medicines, file, indent=4)
            
class PharmacyManagementSystemGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Pharmacy Management System")
        self.data_file = "pharmacy_data.json"
        self.bg_image = tk.PhotoImage(file="background.png")

        self.pharmacy_system = PharmacyManagementSystem(self.data_file)

        self.initialize_gui()

    def initialize_gui(self):
        #Create a label to display the background image
        bg_label = tk.Label(self.root, image=self.bg_image)
        bg_label.place(relwidth=1, relheight=1)  

        title_font = ("Arial", 24)
        label_bg_color = "#3498db"  # Background color for the label

        self.label = tk.Label(self.root, text="Pharmacy Management System Menu", font=title_font, bg=label_bg_color, fg="white")
        self.label.pack(fill=tk.BOTH, padx=20, pady=10)

        button_font = ("Arial", 16)

        # Add Medicine Button
        add_button = tk.Button(self.root, text="Add Medicine", command=self.add_medicine, font=button_font)
        add_button.pack(pady=(20))

        # Delete Medicine Button
        delete_button = tk.Button(self.root, text="Delete Medicine", command=self.delete_medicine, font=button_font)
        delete_button.pack(pady=20)

        # Edit Medicine Button
        edit_button = tk.Button(self.root, text="Edit Medicine", command=self.edit_medicine, font=button_font)
        edit_button.pack(pady=20)

        # Sale Button
        sale_button = tk.Button(self.root, text="Sell Medicine", command=self.sell_medicine, font=button_font)
        sale_button.pack(pady=20)

        # Display Inventory Button
        display_button = tk.Button(self.root, text="Display Inventory", command=self.display_inventory, font=button_font)
        display_button.pack(pady=20)

        # Quit Button
        quit_button = tk.Button(self.root, text="Quit", command=self.root.quit, font=button_font)
        quit_button.pack(pady=20)


    def add_medicine(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Medicine")
        add_window.geometry("400x300")

        # Create a label to display the "Add Medicine" window background image
        add_bg_label = tk.Label(add_window, image=self.bg_image)
        add_bg_label.place(relwidth=1, relheight=1)

        name_label = tk.Label(add_window, text="Medicine Name:")
        name_label.pack()
        name_entry = tk.Entry(add_window)
        name_entry.pack()

        cost_label = tk.Label(add_window, text="Cost:")
        cost_label.pack()
        cost_entry = tk.Entry(add_window)
        cost_entry.pack()

        quantity_label = tk.Label(add_window, text="Quantity:")
        quantity_label.pack()
        quantity_entry = tk.Entry(add_window)
        quantity_entry.pack()

        type_label = tk.Label(add_window, text="Type:")
        type_label.pack()
        type_entry = tk.Entry(add_window)
        type_entry.pack()

        brand_label = tk.Label(add_window, text="Brand:")
        brand_label.pack()
        brand_entry = tk.Entry(add_window)
        brand_entry.pack()

        add_button = tk.Button(add_window, text="Add", command=lambda: self.add_medicine_to_file(name_entry.get(), float(cost_entry.get()), int(quantity_entry.get()), type_entry.get(), brand_entry.get()))
        add_button.pack()

         # Bind the Enter key press event to trigger the "Add" button
        add_window.bind('<Return>', lambda event=None: add_button.invoke())


    def add_medicine_to_file(self, name, cost, quantity, med_type, brand):
        name = name.lower()  # Convert the name to lowercase for consistency
        if name not in self.pharmacy_system.medicines:
            self.pharmacy_system.medicines[name] = {
                "cost": cost,
                "quantity": quantity,
                "type": med_type,
                "brand": brand
            }
            self.pharmacy_system.save_data()  # Save the updated data
            print(f"Medicine '{name}' added to inventory.")
        else:
            print(f"Error: Medicine '{name}' already exists in inventory.")
            
    def delete_medicine(self):
        delete_window = tk.Toplevel(self.root)
        delete_window.title("Delete Medicine")
        delete_window.geometry("400x300")

        # Create a label to display the "Delete Medicine" window background image
        add_bg_label = tk.Label(delete_window, image=self.bg_image)
        add_bg_label.place(relwidth=1, relheight=1)

        name_label = tk.Label(delete_window, text="Medicine Name:")
        name_label.pack()
        name_entry = tk.Entry(delete_window)
        name_entry.pack()

        delete_button = tk.Button(delete_window, text="Delete", command=lambda: self.delete_medicine_from_file(name_entry.get().lower()))
        delete_button.pack()

        # Bind the Enter key press event to trigger the "Delete" button
        delete_window.bind('<Return>', lambda event=None: delete_button.invoke())

    def delete_medicine_from_file(self, name):
        name = name.lower()  # Convert the entered medicine name to lowercase
        real_name = None  # Initialize a variable to store the real name
        for n in self.pharmacy_system.medicines:
            if n.lower() == name:
                real_name = n
                break
        if real_name:
            self.pharmacy_system.delete_medicine(real_name)
        else:
            print(f"Error: Medicine '{name}' not found in inventory")


    def edit_medicine(self):
        edit_window = tk.Toplevel(self.root)
        edit_window.title("Edit Medicine")
        edit_window.geometry("400x300")

        # Create a label to display the "Edit Medicine" window background image
        add_bg_label = tk.Label(edit_window, image=self.bg_image)
        add_bg_label.place(relwidth=1, relheight=1)

        # Add your entry fields and buttons as needed
        name_label = tk.Label(edit_window, text="Medicine Name:")
        name_label.pack()
        name_entry = tk.Entry(edit_window)
        name_entry.pack()

        cost_label = tk.Label(edit_window, text="Cost:")
        cost_label.pack()
        cost_entry = tk.Entry(edit_window)
        cost_entry.pack()

        quantity_label = tk.Label(edit_window, text="Quantity:")
        quantity_label.pack()
        quantity_entry = tk.Entry(edit_window)
        quantity_entry.pack()

        type_label = tk.Label(edit_window, text="Type:")
        type_label.pack()
        type_entry = tk.Entry(edit_window)
        type_entry.pack()

        brand_label = tk.Label(edit_window, text="Brand:")
        brand_label.pack()
        brand_entry = tk.Entry(edit_window)
        brand_entry.pack()

        edit_button = tk.Button(edit_window, text="Edit", command=lambda: self.edit_medicine_in_file(name_entry.get(), float(cost_entry.get()), int(quantity_entry.get()), type_entry.get(), brand_entry.get()))
        edit_button.pack()

         # Bind the Enter key press event to trigger the "Edit" button
        edit_window.bind('<Return>', lambda event=None: edit_button.invoke())


    def edit_medicine_in_file(self, name, med_type, brand, cost, quantity):
        name = name.lower()  # Convert the entered medicine name to lowercase
        real_name = None  # Initialize a variable to store the real name
        for n in self.pharmacy_system.medicines:
            if n.lower() == name:
                real_name = n
                break
        if real_name:
            self.pharmacy_system.edit_medicine(real_name, med_type, brand, cost, quantity)
        else:
            print(f"Error: Medicine '{name}' not found in inventory")

    def sell_medicine(self):
        sell_window = tk.Toplevel(self.root)
        sell_window.title("Sell Medicine")
        sell_window.geometry("400x200")

        # Create a label to display the "Sell Medicine" window background image
        sell_bg_label = tk.Label(sell_window, image=self.bg_image)
        sell_bg_label.place(relwidth=1, relheight=1)

        name_label = tk.Label(sell_window, text="Medicine Name:")
        name_label.pack()
        name_entry = tk.Entry(sell_window)
        name_entry.pack()

        quantity_label = tk.Label(sell_window, text="Quantity Sold:")
        quantity_label.pack()
        quantity_entry = tk.Entry(sell_window)
        quantity_entry.pack()

        sell_button = tk.Button(sell_window, text="Sell", command=lambda: self.sell_medicine_from_inventory(name_entry.get().lower(), int(quantity_entry.get())))
        sell_button.pack()
        sell_window.bind('<Return>', lambda event=None: sell_button.invoke())

    def sell_medicine_from_inventory(self, name, quantity_sold):
        name = name.lower()  # Convert the entered medicine name to lowercase
        if name in (n.lower() for n in self.pharmacy_system.medicines):
            for real_name, info in self.pharmacy_system.medicines.items():
                if name.lower() == real_name.lower():  # Convert the name in the inventory to lowercase for comparison
                    current_quantity = info["quantity"]
                    if current_quantity >= quantity_sold:
                        new_quantity = current_quantity - quantity_sold
                        self.pharmacy_system.medicines[real_name]["quantity"] = new_quantity
                        print(f"{quantity_sold} units of {real_name} sold. Updated quantity: {new_quantity}")
                        self.pharmacy_system.save_data()  # Save the updated data
                        return
                    else:
                        print(f"Error: Not enough {real_name} in inventory")
                        return
        else:
            print(f"Error: Medicine '{name}' not found in inventory")

    def display_inventory(self):
        display_window = tk.Toplevel(self.root)
        display_window.title("Inventory")
        display_window.geometry("1000x800")

        self.search_entry = tk.Entry(display_window)
        self.search_entry.pack(pady=10)
        search_button = tk.Button(display_window, text="Search", command=self.search_inventory)
        search_button.pack()
        self.search_entry.bind('<Return>', lambda event=None: self.search_inventory())

        # Add two sorting buttons within the inventory window
        alpha_sort_button = tk.Button(display_window, text="Sort Alphabetically", command=self.sort_alphabetically)
        alpha_sort_button.pack(pady=10)

        last_added_sort_button = tk.Button(display_window, text="Sort by Last Added", command=self.sort_by_last_added)
        last_added_sort_button.pack(pady=10)

        self.inventory_tree = ttk.Treeview(display_window, columns=("S.No", "Name", "Type", "Brand", "Cost", "Quantity",))

        # Define the columns
        self.inventory_tree.heading("#1", text="S.No")
        self.inventory_tree.heading("#2", text="Name")
        self.inventory_tree.heading("#3", text="Type")
        self.inventory_tree.heading("#4", text="Brand")
        self.inventory_tree.heading("#5", text="Cost")
        self.inventory_tree.heading("#6", text="Quantity")

        # Add a custom style to make the table more attractive
        style = ttk.Style()
        style.configure("Treeview.Heading", background="skyblue", foreground="black", font=("Arial", 12, "bold"))
        style.configure("Treeview", background="lightcyan", fieldbackground="lightcyan")

        # Clear the existing items in the Treeview
        self.inventory_tree.delete(*self.inventory_tree.get_children())

        # Insert data into the Treeview with serial numbers
        for i, (name, info) in enumerate(self.pharmacy_system.medicines.items(), start=1):
            data = (i, name, info['type'], info['brand'], info['cost'], info['quantity'])  # Change 'count' to 'quantity'
            self.inventory_tree.insert("", "end", values=data)

        # Pack the Treeview widget
        self.inventory_tree.pack(expand=True, fill="both")
        separator = ttk.Separator(display_window, orient="horizontal")
        separator.pack(fill="x")

        # Set column widths
        self.inventory_tree.column("#1", width=10) 
        self.inventory_tree.column("#2", width=200)
        self.inventory_tree.column("#3", width=50)
        self.inventory_tree.column("#4", width=150)
        self.inventory_tree.column("#5", width=50)
        self.inventory_tree.column("#6", width=50)
        self.inventory_tree.pack(expand=True, fill="both")
        self.inventory_tree.column('#0',width=0)
        separator = ttk.Separator(display_window, orient="horizontal")
        separator.pack(fill="x")

        self.display_inventory_with_data(self.pharmacy_system.medicines)

    def sort_alphabetically(self):
        # Sort the medicines alphabetically by their names
        sorted_medicines = dict(sorted(self.pharmacy_system.medicines.items(), key=lambda item: item[0].lower()))
        self.display_inventory_with_data(sorted_medicines)

    def sort_by_last_added(self):
        # Sort the medicines by the order they were added (original order)
        self.display_inventory_with_data(self.pharmacy_system.medicines)

    def display_inventory_with_data(self, data):
        # Clear the existing items in the Treeview
        for item in self.inventory_tree.get_children():
            self.inventory_tree.delete(item)

        
        for i, (name, info) in enumerate(data.items(), start=1):
            capitalized_name = name.capitalize()
            data = (i, capitalized_name, info['type'], info['brand'], info['cost'], info['quantity'])
            self.inventory_tree.insert("", "end", values=data) 

    # Add the following method to the PharmacyManagementSystemGUI class
    def search_inventory(self):
        search_text = self.search_entry.get().lower() 
        if not search_text:
            # If the search bar is empty, display the entire inventory
            self.display_inventory()
        else:
            for item in self.inventory_tree.get_children():
                self.inventory_tree.delete(item)
            for i, (name, info) in enumerate(self.pharmacy_system.medicines.items(), start=1):
                if search_text in name.lower():
                    data = (i, name, info['type'], info['brand'], info['cost'], info['quantity'])
                    self.inventory_tree.insert("", "end", values=data)

    def filter_inventory(self):
        search_text = self.search_entry.get().lower()

        # Clear the existing items in the Treeview
        for item in self.inventory_tree.get_children():
            self.inventory_tree.delete(item)

        # Filter and insert the matching data into the Treeview
        for i, (name, info) in enumerate(self.pharmacy_system.medicines.items(), start=1):
            if search_text in name.lower():
                data = (i, name, info['type'], info['brand'], info['cost'], info['quantity'])
                self.inventory_tree.insert("", "end", values=data)

def main():
    root = tk.Tk()
    app = PharmacyManagementSystemGUI(root)
    root.geometry("1200x700")  # Set the width and height to your preferred values
    root.mainloop()

if __name__ == "__main__":
    main()



"""
----------------------------------------------------------------------------------------------------
 Done by - Babin Joe
 Github - https://github.com/BABIN-JOE/
----------------------------------------------------------------------------------------------------
"""