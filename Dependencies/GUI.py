import tkinter as tk
from tkinter import ttk

#Initial Window Size Configuration
INITIAL_WIDTH = 1600
INITIAL_HEIGHT = 800

#Menu Columns and Rows
MENU_ROWS = 10
MENU_COLUMNS = 5

#Function to add Item to Menu Grid
def add_grid_item(item):
    command = lambda:order_list.insert(tk.END, item)

    grid_position = len(order_left_frame.winfo_children())
    grid_button = ttk.Button(order_left_frame, text=item, command=command)
    row = grid_position // MENU_COLUMNS
    column = grid_position % MENU_COLUMNS
    grid_button.grid(row=row, column=column, sticky="nesw", padx=10, pady=10)

#Function to add sizes to Edit Menu
def add_sizes(sizes):
    size_list_frame.columnconfigure(0, weight=1)
    for i, size in enumerate(sizes):
        size_list_frame.rowconfigure(i, weight=1)
        size_radio = ttk.Radiobutton(size_list_frame, text=size, variable="size", value=size)
        size_radio.grid(row=i, column=0)

#Function to add Add-Ins to Edit Menu
def add_add_ins(add_ins):
    
    row_count = (len(add_ins) // 3) + 1
    for row in range(row_count):
        add_ins_frame.rowconfigure(row, weight=1)
    for i, add_in in enumerate(add_ins):
        add_check_state[add_in] = tk.IntVar()
        add_in_check = ttk.Checkbutton(add_ins_frame, text=add_in, variable=add_check_state[add_in])
        row = i // 3
        column = i % 3
        add_in_check.grid(row=row, column=column, sticky="nesw", padx=3, pady=3)


#Main Window Configuration
root = tk.Tk()
root.title('Drink Factory Ordering')
root.iconbitmap('dependencies\drink_factory_logo.ico')
root.geometry(f'{INITIAL_WIDTH}x{INITIAL_HEIGHT}')

#Style Configuration
style = ttk.Style(root)
style.configure("TRadiobutton", font=("Helvetica", 60))
style.configure("TCheckbutton", font=("Helvetica", 20))

#Menu Selection
menus = ttk.Notebook(root)
menus.place(relwidth=1, relheight=1)

#Ordering Menu Config
order_menu = tk.Frame(menus)
order_menu.place(relheight=1, relwidth=1)
menus.add(order_menu, text="Order")

#Ordering Menu Right Frame Config
order_right_frame = tk.Frame(order_menu)
order_right_frame.place(relheight=1, relwidth=.25, relx=.75)

#Ordering Menu Left Frame Config
order_left_frame = tk.Frame(order_menu)
order_left_frame.place(relheight=1, relwidth=.75)

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
order_list = tk.Listbox(order_list_frame)
order_list.pack(padx=10, pady=10, expand=True, fill="both")

#Submit Button
submit_button = ttk.Button(order_control, text="Submit")
submit_button.grid(row=1, column=0, columnspan=2, sticky="nesw", padx=5, pady=5)

#Edit Button
edit_button = ttk.Button(order_control, text="Edit")
edit_button.grid(row=0, column=0, sticky="nesw", padx=5, pady=5)

#Delete Button
delete_command = lambda:order_list.delete(order_list.curselection())
delete_button = ttk.Button(order_control, text="Delete", command=delete_command)
delete_button.grid(row=0, column=1, sticky="nesw", padx=5, pady=5)

#Menu Buttons Config
for row in range(MENU_ROWS):
    order_left_frame.rowconfigure(row, weight=1)
for column in range(MENU_COLUMNS):
    order_left_frame.columnconfigure(column, weight=1)

#Item Editing Menu
edit_menu = tk.Frame(menus)
edit_menu.place(relheight=1, relwidth=1)
menus.add(edit_menu, text="Edit")

#Size List Frame Config
size_list_frame = tk.Frame(edit_menu)
size_list_frame.place(relheight=1, relwidth=.2)

#Add-Ins Frame Config
add_ins_frame = tk.Frame(edit_menu)
add_ins_frame.place(relheight=1, relwidth=.6, relx=.2)
for column in range(3):
    add_ins_frame.columnconfigure(column, weight=1)

add_check_state = {}


