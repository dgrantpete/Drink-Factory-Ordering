import tkinter as tk
from tkinter import ttk

#Initial Window Size Configuration
INITIAL_WIDTH = 1600
INITIAL_HEIGHT = 800

#Main Window Configuration
root = tk.Tk()
root.title('Drink Factory Ordering')
root.iconbitmap('dependencies\drink_factory_logo.ico')
root.geometry(f'{INITIAL_WIDTH}x{INITIAL_HEIGHT}')

#Menu Selection
menus = ttk.Notebook(root)
menus.place(relwidth=1, relheight=1)

#Ordering Menu Config
order_menu = tk.Frame(root)
order_menu.place(relheight=1, relwidth=1)

#Ordering Menu Right Frame Config
order_right_frame = tk.Frame(order_menu, bg="blue")
order_right_frame.place(relheight=1, relwidth=.25, relx=.75)

#Order Control Button Grid Config
order_control = tk.Frame(order_right_frame, bg="red")
order_control.place(relheight=.3, relwidth=1, rely=.7)

order_control.columnconfigure()


root.mainloop()