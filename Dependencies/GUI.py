import tkinter as tk
from tkinter import ttk

#Initial Window Size Configuration
INITIAL_WIDTH = 1600
INITIAL_HEIGHT = 800

#Menu Columns and Rows
MENU_ROWS = 6
MENU_COLUMNS = 3

#Main Window Configuration
root = tk.Tk()
root.title('Drink Factory Ordering')
root.iconbitmap('dependencies\drink_factory_logo.ico')
root.geometry(f'{INITIAL_WIDTH}x{INITIAL_HEIGHT}')

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

#Order Control Button Grid Config
order_control = tk.Frame(order_right_frame)
order_control.place(relheight=.3, relwidth=1, rely=.7)

for row in range(2):
    order_control.rowconfigure(row, weight=1)

for column in range(2):
    order_control.columnconfigure(column, weight=1)

#Submit Button
submit_button = ttk.Button(order_control, text="Submit")
submit_button.grid(row=1, column=0, columnspan=2, sticky="nesw", padx=5, pady=5)

#Edit Button
edit_button = ttk.Button(order_control, text="Edit")
edit_button.grid(row=0, column=0, sticky="nesw", padx=5, pady=5)

#Delete Button
delete_button = ttk.Button(order_control, text="Delete")
delete_button.grid(row=0, column=1, sticky="nesw", padx=5, pady=5)

#Menu Buttons Config
for row in range(MENU_ROWS):
    order_left_frame.rowconfigure(row, weight=1)
for column in range(MENU_COLUMNS):
    order_left_frame.columnconfigure(column, weight=1)
for row in range(MENU_ROWS):
    for column in range(MENU_COLUMNS):
        ttk.Button(order_left_frame, text="test").grid(row=row, column=column, sticky="nesw", padx=10, pady=10)

root.mainloop()