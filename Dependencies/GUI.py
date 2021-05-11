import tkinter as tk

#Initial Window Size Configuration
INITIAL_WIDTH = 1600
INITIAL_HEIGHT = 500

#Function to call GUI
def start_gui():

    #Higher-Level Functions to drive GUI
    def add_list_item(item_string):
        order_list.insert(tk.END, item_string)

    def remove_selected_item():
        order_list.delete(order_list.curselection())
    
    #Main GUI Body
    root = tk.Tk()

    root.geometry(f"{INITIAL_WIDTH}x{INITIAL_HEIGHT}+400+400")
    root.title("Drink Factory Ordering")
    root.iconbitmap("dependencies\drink_factory_logo.ico")

    right_frame = tk.Frame(root)
    right_frame.place(relx=.75, relwidth=.25, relheight=1)

    left_frame = tk.Frame(root)
    left_frame.place(relwidth=.75, relheight=1)

    edit_del_frame = tk.Frame(right_frame)
    edit_del_frame.place(rely=.6, relwidth=1, relheight=.15)
    edit_del_frame.grid_rowconfigure(1, weight=1)
    edit_del_frame.grid_columnconfigure(1, weight=1)
    edit_del_frame.grid_columnconfigure(2, weight=1)

    edit_button = tk.Button(edit_del_frame, text="Edit")
    edit_button.grid(row=1, column=1, sticky="nesw", padx=5, pady=5)

    del_button = tk.Button(edit_del_frame, text="Delete", command=remove_selected_item)
    del_button.grid(row=1, column=2, sticky="nesw", padx=5, pady=5)

    order_list_frame = tk.Frame(right_frame)
    order_list = tk.Listbox(order_list_frame, font=30)
    order_list_frame.place(relwidth=1, relheight=.6)
    order_list.pack(expand=True, padx=10, pady=10, fill="both")
    for number in range(10):
        add_list_item(number)

    submit_button_frame = tk.Frame(right_frame)
    submit_button = tk.Button(submit_button_frame, text = "Submit")
    submit_button_frame.place(relwidth=1, relheight=0.25, rely=.75)
    submit_button.pack(expand=True, padx=5, pady=5, fill="both")

    for row in range(5):
        left_frame.grid_rowconfigure(row, weight=1)
        for column in range(3):
            (tk.Button(left_frame)).grid(row=row, column=column)
            if row == 0:
                left_frame.grid_columnconfigure(column, weight=1)

    root.mainloop()
