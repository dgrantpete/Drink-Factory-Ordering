import os
import pandas as pd
import pathlib
from tkinter import *

root = Tk()


#MenuItem class represents default items on Menu
class MenuItem:
    def __init__(self, item_name, *adds):
        self.item_name = item_name
        self.add_ins = [add.lower() for add in adds if type(add)==str]

            
    def __str__(self):
        return self.item_name + ' with ' + str(self.add_ins)
        
    def __repr__(self):
        return 'MenuItem object ' + self.item_name

#OrderItem class represents MenuItem as they are ordered
class OrderItem:
    def __init__(self, size, drink, base, *adds):
        self.size = size
        self.price = prices[size] + (len(adds)*prices['Add-In'])
        self.add_ins = drinks[drink].add_ins
        self.drink_type = drink
        for add_in in adds:
            if not type(add_in) == str:
                raise TypeError('Add-in must be of type "str"')
            elif add_in.lower() in self.add_ins:
                print(add_in.capitalize() + ' is already in this drink.')
            elif add_in.lower() in add_ins_list:
                self.add_ins += [add_in.lower()]
            else:
                print(add_in.capitalize() + ' is not in "add_ins_list".')
        self.base = base
    def __str__(self):
        return f'A(n) {self.base} {self.drink_type} with {self.add_ins} costing ${self.price}.'
        
class Order:
    pass

#Locating local file path, importing menu (stored in a csv format) and prices
file_path = pathlib.Path(__file__)
local_path = file_path.parent
menu_file = local_path/'base_drinks.csv'
prices_file = local_path/'prices.csv'

#Transferring prices from CSV to dictionary
prices_df = pd.read_csv(prices_file)
prices = {}
for item, price in prices_df.values:
    prices[item] = price

#CSV to DataFrame and converting add-ins to list
drink_menu = pd.read_csv(menu_file)
add_in_matrix = drink_menu.iloc[:,1:]
add_ins_list = []
for row in add_in_matrix:
    for add_in in add_in_matrix[row]:
        if (add_in in add_ins_list) or type(add_in) == float:
            continue
        elif add_in not in add_ins_list:
            add_ins_list.append(add_in.lower())
add_ins_list = sorted(add_ins_list)

#Converting drink names from CSV file to MenuItem Object with attached data
drinks = {}
for drink_index in drink_menu.index:
    drinks[drink_menu.iloc[drink_index, 0]] = MenuItem(*drink_menu.iloc[drink_index])

myButton = Button(root, text='test')
myButton.pack()
root.mainloop()