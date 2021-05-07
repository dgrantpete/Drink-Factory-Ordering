import tkinter as tk
import LabelPrinting

INITIAL_WIDTH = 1600
INITIAL_HEIGHT = 500

root = tk.Tk()
root.geometry(f"{INITIAL_WIDTH}x{INITIAL_HEIGHT}+400+400")

right_frame = tk.Frame(root)
right_frame.place(relx=1, rely=1, relwidth=.25, relheight=1, anchor="se")

order_list_frame = tk.Frame(right_frame)
order_list = tk.Listbox(order_list_frame, font=30)
order_list_frame.place(relwidth=1, relheight=.75)
order_list.pack(expand=True, padx=10, pady=10, fill="both")
for number in range(10):
    order_list.insert(tk.END, number)

submit_button_frame = tk.Frame(right_frame)
submit_button = tk.Button(submit_button_frame, text = "Submit", cursor="hand2")
submit_button_frame.place(relwidth=1, relheight=0.25, rely=.75)
submit_button.pack(expand=True, padx=20, pady=20, fill="both")


root.mainloop()