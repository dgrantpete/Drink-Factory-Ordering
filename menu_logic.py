import os
import json
from Dependencies import LabelPrinting

#class to Store Imported Menu Info
class Menu:
    def __init__(self, menu_base_drinks, menu_add_ins, menu_add_in_price, menu_sizes):
        self.base_drinks = menu_base_drinks
        self.add_ins = menu_add_ins
        self.add_in_price = menu_add_in_price
        self.sizes = menu_sizes

#class Representing Customized Order Items
class OrderItem:
    def __init__(self, base_item, size, item_add_ins=None):
        if item_add_ins is None:
            add_ins = []
        self.base_item = base_item
        self.size = size
        self.add_ins = item_add_ins
        self.price = menu.sizes[size] + (len(item_add_ins) * menu.add_in_price)

    def __str__(self):
        return f'{self.size} {self.base_item} +{", ".join(self.add_ins)}'
    
    def summary(self):
        summary = f"{self.size}\n{self.base_item}"
        for add_in in self.add_ins:
            summary += f"\n+{add_in}"
        summary += f"\n{self.price}"
        return summary

class CurrentOrderItem:
    def __init__(self):
        self.base_item = None

#Importing Menu Information and converting to dictionaries
def menu_import():
    with open("menu.json") as menu_file:
        json_data = json.load(menu_file)
        sizes = json_data["prices"]["sizes"]
        base_drinks = json_data["base drinks"]
        add_in_price = json_data["prices"]["Add-In"]

    #Temporary Add-In List
    add_ins_list = set()
    for drink in base_drinks.values():
        add_ins_list |= set(drink)
    add_ins_list = sorted(list(add_ins_list))

    return Menu(base_drinks, add_ins_list, add_in_price, sizes)

menu = menu_import()