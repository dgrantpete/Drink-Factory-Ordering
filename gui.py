import tkinter as tk
import LabelPrinting

INITIAL_WIDTH = 1600
INITIAL_HEIGHT = 500

def add_list_item(item_string):
    order_list.insert(tk.END, item_string)

def remove_selected_item():
    pass
    order_list.delete(order_list.curselection())

root = tk.Tk()
root.geometry(f"{INITIAL_WIDTH}x{INITIAL_HEIGHT}+400+400")


right_frame = tk.Frame(root)
right_frame.place(relx=.75, relwidth=.25, relheight=1)

left_frame = tk.Frame(root)
left_frame.place(relwidth=.75)

edit_del_frame = tk.Frame(right_frame, bg="blue")
edit_del_frame.place(rely=.6, relwidth=1, relheight=.15)
edit_del_frame.grid_rowconfigure(1, weight=1)
edit_del_frame.grid_columnconfigure(1, weight=1)
edit_del_frame.grid_columnconfigure(2, weight=1)

edit_button = tk.Button(edit_del_frame, text="Edit")
edit_button.grid(row=1, column=1, sticky="nesw")

del_button = tk.Button(edit_del_frame, text="Delete", command=remove_selected_item)
del_button.grid(row=1, column=2, sticky="nesw")

order_list_frame = tk.Frame(right_frame)
order_list = tk.Listbox(order_list_frame, font=30)
order_list_frame.place(relwidth=1, relheight=.6)
order_list.pack(expand=True, padx=10, pady=10, fill="both")
for number in range(10):
    add_list_item(number)


submit_button_frame = tk.Frame(right_frame)
submit_button = tk.Button(submit_button_frame, text = "Submit", cursor="hand2", command=remove_selected_item)
submit_button_frame.place(relwidth=1, relheight=0.25, rely=.75)
submit_button.pack(expand=True, padx=20, pady=20, fill="both")


root.mainloop()