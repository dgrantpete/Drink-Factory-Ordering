import tkinter as tk
from tkinter import ttk
from menu_logic import menu_import, ActiveOrder, Menu, OrderItem
from Dependencies.LabelPrinting import print_label
"""

User Configurable Variables

"""

#Font
DEFAULT_FONT = "Verdana"
SM_SIZE = 10
MED_SIZE = 13
LG_SIZE = 25

#Initial Window Size Configuration
INITIAL_WIDTH = 1600
INITIAL_HEIGHT = 800

#Menu Columns and Rows
MENU_ROWS = 10
MENU_COLUMNS = 5

#Edit Menu Add-In Columns
ADD_IN_COLUMNS = 3

"""

GUI Driving Functions

"""

#Adds single item to Menu Grid
def add_grid_item(item):
    command = lambda: drink_new(item)

    grid_position = len(order_left_frame.winfo_children())
    grid_button = ttk.Button(order_left_frame, text=item, command=command)
    row = grid_position // MENU_COLUMNS
    column = grid_position % MENU_COLUMNS
    grid_button.grid(row=row, column=column, sticky="nesw", padx=10, pady=10)

#Adds sizes to Edit Menu
def add_sizes(sizes):
    size_list_frame.columnconfigure(0, weight=1)
    for size in sizes:
        size_radio = ttk.Radiobutton(size_list_frame, text=size, variable=size_variable, value=size)
        size_radio.pack(expand=True, fill="both")

#Adds Soda Options to Edit Menu
def add_sodas(sodas):
    size_list_frame.columnconfigure(0, weight=1)
    for soda in sodas:
        soda_radio = ttk.Radiobutton(base_sodas_frame, text=soda, variable=soda_variable, value=soda)
        soda_radio.pack(expand=True, fill="both")

#Adds Add-Ins to Edit Menu
def add_add_ins(add_ins):
    row_count = (len(add_ins) // ADD_IN_COLUMNS) + 1
    for row in range(row_count):
        add_ins_frame.rowconfigure(row, weight=1)
    for i, add_in in enumerate(add_ins):
        add_check_state[add_in] = tk.IntVar()
        add_in_check = ttk.Checkbutton(add_ins_frame, text=add_in, variable=add_check_state[add_in])
        row = i // ADD_IN_COLUMNS
        column = i % ADD_IN_COLUMNS
        add_in_check.configure()
        add_in_check.grid(row=row, column=column, sticky="nesw")

#Returns a List of Selected Add-Ins
def return_add_ins():
    current_add_ins = []
    for add_in, result in add_check_state.items():
        if result.get() == 1:
            current_add_ins.append(add_in)
    return current_add_ins

#Clears Edit Menu Selections
def clear_edit_menu():
    for value in add_check_state.values():
        value.set(0)
    size_variable.set("")
    soda_variable.set("")

#Creates New Drink in Edit Menu
def drink_new(drink):
    clear_edit_menu()
    active_order.current_item_base = drink
    for add_in in menu.base_drinks[drink]:
        (add_check_state[add_in]).set(1)
    menus.select(edit_menu)
    return drink

#Sets Edit Menu to Options Specified by OrderItem object
def drink_edit(order_item):
    clear_edit_menu()
    active_order.current_item_base = order_item.base_item
    size_variable.set(order_item.size)
    soda_variable.set(order_item.soda)
    for add_in in order_item.add_ins:
        (add_check_state[add_in]).set(1)
    menus.select(edit_menu)

#Returns OrderItem Object with Options Specified in Edit Menu
def return_active_item():
    return OrderItem(active_order.current_item_base, size_variable.get(), soda_variable.get(), return_add_ins())

#Adds Drink with Currently Selected Options to Order List and Prints Label
def add_active_item(print_drink_label=True):
    active_drink = return_active_item()
    active_order.add_to_order(active_drink)
    if print_drink_label:
        print_label(active_drink.summary())
    menus.select(order_menu)
    menus.hide(edit_menu)
    clear_edit_menu()

add_active_no_label = lambda:add_active_item(print_drink_label=False)

#Opens Edit Menu Configured to Selected Item
def edit_selected():
    drink_edit(active_order.order_items[order_list.curselection()[0]])
    remove_selected()

#Delete Selected Item from ActiveOrder and order_list
def remove_selected():
    active_order.remove_from_order(active_order.order_items[order_list.curselection()[0]])

#Generates Final Order Summary for Confirmation Screen
def generate_order_summary():
    prices_label_text = "\n"
    items_label_text = "\n"
    for item, price in active_order.order_summary():
        prices_label_text += f"{price}\n"
        items_label_text += f"{item}\n"
    prices_summary_variable.set(prices_label_text)
    items_summary_variable.set(items_label_text)
    total_variable.set(f"Total: {active_order.total()}")
    menus.select(confirm_menu)
    
    
        

"""

Root Configuration

"""

#Main Window Configuration
root = tk.Tk()
root.title('Drink Factory Ordering')
root.iconbitmap('dependencies\drink_factory_logo.ico')
root.geometry(f'{INITIAL_WIDTH}x{INITIAL_HEIGHT}')

#Style Configuration
style = ttk.Style(root)
style.configure(".", font=(DEFAULT_FONT, MED_SIZE))
style.configure("TCheckbutton", background="#ebebeb")
style.configure("TRadiobutton", background="#ebebeb", font=(DEFAULT_FONT, LG_SIZE))

style.map("TCheckbutton",
    foreground=[('selected', 'red')],
    background=[('selected', '#b0b0b0')]
    )

style.map("TRadiobutton",
    foreground=[('selected', 'red')],
    background=[('selected', '#b0b0b0')]
    )


"""

Menus Configuration

"""

menu = menu_import()

#Menu Selection
menus = ttk.Notebook(root)
menus.place(relwidth=1, relheight=1)

#Ordering Menu Config
order_menu = tk.Frame(menus)
order_menu.place(relheight=1, relwidth=1)
menus.add(order_menu, text="Order")

#Editing Menu Config
edit_menu = tk.Frame(menus)
edit_menu.place(relheight=1, relwidth=1)
menus.add(edit_menu, text="Edit")
menus.hide(edit_menu)

#Confirmation Menu Config
confirm_menu = tk.Frame(menus)
confirm_menu.place(relheight=1, relwidth=1)
menus.add(confirm_menu, text="Confirmation")

"""

Ordering Menu Setup

"""

#Ordering Menu Right Frame Config
order_right_frame = tk.Frame(order_menu)
order_right_frame.place(relheight=1, relwidth=.4, relx=.6)

#Ordering Menu Left Frame Config
order_left_frame = tk.Frame(order_menu)
order_left_frame.place(relheight=1, relwidth=.6)

#Adding Menu Buttons for Drinks
for drink in menu.base_drinks:
    add_grid_item(drink)

#Ordering Menu List Frame Config
order_list_frame = tk.Frame(order_right_frame)
order_list_frame.place(relheight=0.7, relwidth=1)

#Order Control Button Grid Config
order_control = tk.Frame(order_right_frame)
order_control.place(relheight=.3, relwidth=1, rely=.7)

for row in range(2):
    order_control.rowconfigure(row, weight=1)

for column in range(2):
    order_control.columnconfigure(column, weight=1)

#Order List
order_list = tk.Listbox(order_list_frame, font=10)
order_list.pack(padx=10, pady=10, expand=True, fill="both")

#Submit Button
submit_button = ttk.Button(order_control, text="Submit", command=generate_order_summary)
submit_button.grid(row=1, column=0, columnspan=2, sticky="nesw", padx=5, pady=5)

#Edit Button
edit_button = ttk.Button(order_control, text="Edit", command=edit_selected)
edit_button.grid(row=0, column=0, sticky="nesw", padx=5, pady=5)

#Delete Button
delete_button = ttk.Button(order_control, text="Delete", command=remove_selected)
delete_button.grid(row=0, column=1, sticky="nesw", padx=5, pady=5)

#Menu Item Buttons Config
for row in range(MENU_ROWS):
    order_left_frame.rowconfigure(row, weight=1)
for column in range(MENU_COLUMNS):
    order_left_frame.columnconfigure(column, weight=1)

"""

Edit Menu Setup

"""

#Size List Frame Config
size_list_frame = ttk.LabelFrame(edit_menu, text="Size")
size_list_frame.place(relheight=.7, relwidth=.2, relx=.8)

size_variable = tk.StringVar()

#Adding Drink Sizes to Edit Menu
add_sizes(menu.sizes)

#Add-Ins Frame Config
add_ins_frame = ttk.LabelFrame(edit_menu, text="Add-Ins")
add_ins_frame.place(relheight=1, relwidth=.6, relx=.2)
for column in range(3):
    add_ins_frame.columnconfigure(column, weight=1)

#Adding Add-Ins to Edit Menu
add_check_state = {}
add_add_ins(menu.add_ins)

#Base Sodas Frame Config
base_sodas_frame = ttk.LabelFrame(edit_menu, text="Base Soda")
base_sodas_frame.place(relwidth=0.2, relheight=1)

soda_variable = tk.StringVar()

#Adding Sodas to Edit Menu
add_sodas(menu.sodas)

#Edit Menu Submit Button Frame
edit_submit_frame = tk.Frame(edit_menu)
edit_submit_frame.place(relheight=.3, relwidth=.2, relx=.8, rely=.7)

#Edit Menu Submit Button
edit_submit = ttk.Button(edit_submit_frame, text="Submit", command=add_active_item)
edit_submit.pack(padx=5, pady=5, expand=True, fill="both")

#Edit Menu Submit Button (No Label)
edit_submit = ttk.Button(edit_submit_frame, text="Submit (No Label)", command=add_active_no_label)
edit_submit.pack(padx=5, pady=5, expand=True, fill="both")

"""

Confirmation Menu Setup

"""

#Order Summary Frame
summary_frame = ttk.LabelFrame(confirm_menu, text="Order Summary", labelanchor="n")
summary_frame.place(relwidth=.5, relheight=.7)

#Order Summary Items

items_summary_variable = tk.StringVar()

items_summary = ttk.Label(summary_frame, textvar=items_summary_variable, anchor="nw", font=(DEFAULT_FONT, SM_SIZE))
items_summary.place(relwidth=.9, relheight=.9)

#Order Summary Prices

prices_summary_variable = tk.StringVar()

prices_summary = ttk.Label(summary_frame, textvar=prices_summary_variable, anchor="ne", font=(DEFAULT_FONT, SM_SIZE))
prices_summary.place(relwidth=.1, relheight=.9, relx=.9)

#Order Total

total_variable = tk.StringVar()

total_label = ttk.Label(summary_frame, textvar=total_variable, anchor="center")
total_label.place(relwidth=1, relheight=.1, rely=.9)


"""

Menu Data Configuration

"""

active_order = ActiveOrder(order_list)

root.mainloop()
