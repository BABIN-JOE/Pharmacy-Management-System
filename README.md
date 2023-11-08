## Pharmacy-Management-System

    The Pharmacy Management System is a Python-based application for managing pharmacy inventory. It provides a graphical user interface (GUI) for performing           various tasks related to medicines, such as adding, deleting, editing, selling, and displaying the inventory.


# Features 

    Add Medicine: Easily add new medicines to the inventory, providing details like name, cost, quantity, type, and brand.
    
    Delete Medicine: Remove medicines from the inventory by specifying their names.
    
    Edit Medicine: Update the details of existing medicines, including cost, quantity, type, and brand.
    
    Sell Medicine: Record sales of medicines by specifying the name and quantity sold, and it will automatically update the inventory.
    
    Display Inventory: View the entire inventory, search for specific medicines, and sort the list alphabetically or by the order they were added.


# Requirements
    Python 3.x (https://www.python.org/downloads/)
    Tkinter (usually included with Python) if not use pip install tkinter
    Pillow (PIL) for handling images (optional, install via pip install Pillow)
    Ensure you have Python installed on your system.
    
    If you want to use background images, install the Pillow (PIL) library using the following command:
    pip install Pillow
    Create or provide a data file named "pharmacy_data.json" for storing medicine inventory. The program will load and save data to this file.


# Usage
    Run the program by executing the provided Python script:
    python pharmacy_management_system.py
    The GUI application will open, and you can start managing your pharmacy inventory.


# Troubleshooting
    If you encounter issues with tkinter not being available or other package-related problems, make sure you've installed Python and any required packages as          mentioned in the Requirements section.
    
    Check file paths for images and data files to ensure they are correctly specified in your code.
    The json file and the background image should be in the same directory where your python file is present.


# Contributing
    Feel free to contribute to this project by submitting bug reports, feature requests, or pull requests. Your contributions are highly appreciated!


# Description 
    You can add a medicine, edit a medicine or delete a medicine and even you can update the quantity of medicine if sold, using sell medicine. The Medicine data     contains Medicine Name, Type, Cost, Quantity and Brand Name. This Data's will be stored as a inventory in json file. You can view the inventory using Display     inventory and also you can easily find the required medicine. The inventory has a search bar where you can easily search and find the medicines. It also has 
    a sorting order of medicines like Alphabetic order and Last added order. It is one of the easy and convininet way to store the medicine details in the            Pharmacies.


# Code break
    Import Libraries: The code imports the tkinter library for creating the GUI and other 
    necessary libraries like json.
    
    Main Function: The main() function is the entry point of the program. It creates an instance 
    of the PharmacyManagementSystemGUI class and runs the main event loop.
    
    PharmacyManagementSystem Class: This class represents the backend of the pharmacy 
    management system. It handles the loading and saving of medicine data from/to a JSON file.
    It also provides methods to add, delete, edit, and display medicines in the inventory.
    
    PharmacyManagementSystemGUI Class: This class represents the graphical user interface of 
    the system. It initializes the GUI, including buttons for adding, deleting, editing, selling, and 
    displaying medicines. It also handles the interaction between the user interface and the 
    PharmacyManagementSystem.
    
    GUI Components: The code creates buttons, labels, and entry fields for user interaction and 
    displays the inventory of medicines in a Treeview widget.
    
    Event Handling: Event handlers are set up for the various buttons to trigger actions like 
    adding, deleting, editing, and selling medicines. Additionally, there's a search feature to filter 
    medicines by name.
    
    Display Inventory: The inventory of medicines is displayed in a Treeview widget. Sorting 
    options are provided for alphabetical and original order.
    
    Error Handling: The code includes basic error handling for file operations and user input.
    In summary, the code doesn't implement complex algorithms but rather focuses on building 
    a user-friendly GUI for managing a pharmacy's inventory with functionalities to add, delete, 
    edit, and sell medicines. It also provides basic features for searching and sorting the 
    inventory. The main algorithms involved are those for managing the JSON data file and 
    interacting with the GUI components
    
    CODE BREAKDOWN :
        This code is a Python program that uses the tkinter library to create a graphical user 
        interface (GUI) for a Pharmacy Management System. The GUI allows users to perform 
        various operations related to managing pharmaceutical inventory, including adding, 
        deleting, editing, and selling medicines, as well as displaying the inventory.
        
        Let's break down the code from the top to the bottom, explaining each section and line:
        import tkinter as tk: This line imports the tkinter library and gives it the alias 'tk' to make it 
        easier to work with.
        
        from tkinter import ttk: This line imports a specific module 'ttk' from tkinter, which is used 
        for creating themed widgets.
        import json: This line imports the JSON library, which is used for reading and writing data in 
        JSON format.
        
        def main():: This is the definition of the main function where the program execution starts.
        root = tk.Tk(): This creates the main tkinter application window. It is the root of the GUI.
        root.attributes('-fullscreen', True): This line sets the window to full-screen mode when the 
        application is launched.
        
        class PharmacyManagementSystem:: This defines a class called 
        PharmacyManagementSystem that will handle the data and operations related to the 
        pharmacy inventory.
        
        a. def _init_(self, data_file): This is the constructor method for the class. It takes a data_file 
        argument, which is the name of the JSON file where the inventory data is stored.
        b. self.medicines = {}: This initializes an empty dictionary to store the pharmacy inventory.
        c. self.data_file = data_file: It stores the name of the data file for later use.
        d. self.load_data(): This method is called to load the inventory data from the JSON file when 
        an instance of the class is created.
        e. self.save_data(): This method is used to save the inventory data to the JSON file.
        f. def add_medicine(self, name, cost, quantity, med_type, brand): This method allows adding 
        a new medicine to the inventory. It takes parameters such as the name of the medicine, 
        cost, quantity, type, and brand.
        g. def delete_medicine(self, name): This method allows deleting a medicine from the 
        inventory by its name.
        h. def edit_medicine(self, name, cost, quantity, med_type, brand): This method allows 
        editing the details of a medicine in the inventory.
        i. def get_inventory(self): This method returns a formatted string containing the details of 
        the current inventory.
        j. def load_data(self): This method attempts to load the inventory data from the JSON file. If 
        the file doesn't exist or is empty, it initializes the inventory as an empty dictionary.
        k. def save_data(self): This method saves the inventory data to the JSON file in a formatted 
        manner.
        
        class PharmacyManagementSystemGUI:: This defines a class for the graphical user interface 
        of the pharmacy management system.
        a. def _init_(self, root): This is the constructor method for the GUI class. It takes the main 
        tkinter window 'root' as an argument.
        b. self.root = root: This stores the main tkinter window as an instance variable.
        c. self.root.title("Pharmacy Management System"): This sets the title of the application 
        window.
        d. self.data_file = "pharmacy_data.json": This specifies the name of the JSON data file.
        e. self.bg_image = tk.PhotoImage(file="background.png"): This loads an image file named 
        "background.png" to be used as the background for the GUI.
        f. self.pharmacy_system = PharmacyManagementSystem(self.data_file): This creates an 
        instance of the PharmacyManagementSystem class, initializing it with the data file.
        g. self.initialize_gui(): This method initializes the graphical user interface by creating and 
        configuring widgets.
        
        def initialize_gui(self):: This method sets up the graphical user interface.
        a. bg_label = tk.Label(self.root, image=self.bg_image): This creates a label to display the 
        background image.
        b. self.label = tk.Label(self.root, text="Pharmacy Management System Menu", 
        font=title_font, bg=label_bg_color, fg="white"): This creates a label with a title and 
        formatting for the menu.
        c. self.label.pack(fill=tk.BOTH, padx=20, pady=10): This packs the label widget into the main 
        window.
        d. button_font = ("Arial", 16): This defines a font style for buttons.
        e. The code from here on creates several buttons for different functions, such as adding 
        medicine, deleting medicine, etc., and packs them into the window with appropriate labels 
        and commands.
        
        def add_medicine(self):: This method opens a new window for adding a medicine to the 
        inventory.
        a. add_window = tk.Toplevel(self.root): This creates a new window as a child of the main 
        window.
        b. The method creates labels and entry fields for entering medicine details (name, cost, 
        quantity, type, and brand).
        c. add_button = tk.Button(add_window, text="Add", command=lambda: 
        self.add_medicine_to_file(name_entry.get(), float(cost_entry.get()), 
        int(quantity_entry.get()), type_entry.get(), brand_entry.get())): This creates a button to add 
        the medicine to the inventory and associates it with a command that calls the 
        add_medicine_to_file method with the entered data.
        d. add_window.bind('<Return>', lambda event=None: add_button.invoke()): This binds the 
        Enter key to the "Add" button, allowing the user to press Enter to add the medicine.
        def add_medicine_to_file(self, name, cost, quantity, med_type, brand): This method is called 
        when adding a new medicine. It validates the input, converts the name to lowercase for 
        consistency, and then adds the medicine to the inventory.
        
        def delete_medicine(self):: This method opens a new window for deleting a medicine from 
        the inventory.
        a. Similar to the add method, this method creates a window, labels, an entry field for the 
        medicine name, and a button for deleting.
        b. delete_button = tk.Button(delete_window, text="Delete", command=lambda: 
        self.delete_medicine_from_file(name_entry.get().lower())): This creates a button to delete 
        the medicine and associates it with a command that calls the delete_medicine_from_file 
        method.
        c. delete_window.bind('<Return>', lambda event=None: delete_button.invoke()): This binds 
        the Enter key to the "Delete" button, allowing the user to press Enter to delete the 
        medicine.
        
        def delete_medicine_from_file(self, name): This method deletes a medicine from the 
        inventory and saves the updated data to the JSON file. It first searches for the medicine 
        name in the inventory, taking case-insensitivity into account.
        def edit_medicine(self):: This method opens a new window for editing a medicine in the 
        inventory.
        a. Similar to the previous methods, this method creates a window, labels, entry fields for 
        medicine details, and a button for editing.
        b. edit_button = tk.Button(edit_window, text="Edit", command=lambda: 
        self.edit_medicine_in_file(name_entry.get(), float(cost_entry.get()), 
        int(quantity_entry.get()), type_entry.get(), brand_entry.get())): This creates a button to edit 
        the medicine and associates it with a command that calls the edit_medicine_in_file method.
        c. edit_window.bind('<Return>', lambda event=None: edit_button.invoke()): This binds the 
        Enter key to the "Edit" button, allowing the user to press Enter to edit the medicine.
        def edit_medicine_in_file(self, name, med_type, brand, cost, quantity): This method edits 
        the details of a medicine in the inventory by searching for its name and updating the data.
        
        def sell_medicine(self):: This method opens a new window for selling medicine from the 
        inventory.
        a. Similar to previous methods, this method creates a window, labels, entry fields for 
        medicine name and quantity sold, and a button for selling.
        b. sell_button = tk.Button(sell_window, text="Sell", command=lambda: 
        self.sell_medicine_from_inventory(name_entry.get().lower(), int(quantity_entry.get())): This 
        creates a button to sell the medicine and associates it with a command that calls the 
        sell_medicine_from_inventory method.
        c. sell_window.bind('<Return>', lambda event=None: sell_button.invoke()): This binds the 
        Enter key to the "Sell" button, allowing the user to press Enter to sell the medicine.
        def sell_medicine_from_inventory(self, name, quantity_sold): This method allows selling a 
        specified quantity of a medicine from the inventory. It checks if the medicine exists and has 
        enough quantity to sell.
        
        def display_inventory(self):: This method opens a new window to display the current 
        inventory.
        a. It creates a Treeview widget to display the data in a tabular format.
        b. self.search_entry = tk.Entry(display_window): This creates an entry field for searching 
        within the inventory.
        c. self.search_entry.bind('<Return>', lambda event=None: self.search_inventory()): This binds 
        the Enter key to a method for searching the inventory.
        d. The method also creates buttons for sorting the inventory alphabetically or by the order 
        they were added and associates them with methods for sorting.
        e. It then inserts the inventory data into the Treeview widget and formats the columns and 
        styles for better presentation.
        
        def sort_alphabetically(self):: This method sorts the medicines in the inventory 
        alphabetically by their names and updates the display accordingly.
        def sort_by_last_added(self):: This method keeps the medicines in the original order they 
        were added, updating the display accordingly.
        def display_inventory_with_data(self, data): This method displays the inventory data in the 
        Treeview widget. It clears the existing data, inserts the new data, and sets the column 
        widths.
        def search_inventory(self):: This method is called when searching for specific medicines in 
        the inventory. It filters and displays only the matching medicines.
        def filter_inventory(self):: This method was previously mentioned in the code but is not used 
        or implemented.
        
        def main():: This is the main function where the program execution starts.
        root = tk.Tk(): This creates the main tkinter window.
        app = PharmacyManagementSystemGUI(root): This creates an instance of the GUI class and 
        initializes it with the main window.
        root.geometry("1200x700"): This sets the dimensions of the main window.
        root.mainloop(): This starts the main event loop for the tkinter application, allowing it to 
        respond to user interactions.
        if _name_ == "_main_":: This condition checks if the script is being run as the main program.
        main(): If the condition is met, it calls the main function to start the program.
        
        In summary, this code creates a pharmacy management system with a graphical user 
        interface using tkinter. It allows users to perform various operations on pharmaceutical 
        inventory, including adding, deleting, editing, and selling medicines, as well as displaying the 
        inventory in a tabular format. The data is stored in a JSON file for persistence.
    

# For Queries
    For Queries and errors feel free to contact me. You can also contact me for project related topics and discussions. You can contact me through instagram or       linkedin (Check the bio for contact details). Kindly check and go through it.
