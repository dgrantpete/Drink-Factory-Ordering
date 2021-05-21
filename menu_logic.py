import os
import json
from Dependencies import LabelPrinting

#class Representing Customized Order Items
class OrderItem:
    def __init__(self, base_item, size, add_ins=None):
        if add_ins is None:
            add_ins = []
        self.base_item = base_item
        self.size = size
        self.add_ins = add_ins
        self.price = sizes[size] + (len(add_ins) * add_in_price)

    def __str__(self):
        return f'{self.size} {self.base_item} +{", ".join(self.add_ins)} for {self.price}'
    
    def summary(self):
        summary = f"{self.size}\n{self.base_item}"
        for add_in in self.add_ins:
            summary += f"\n+{add_in}"
        return summary

#Importing Menu Information and converting to dictionaries
sizes = None
base_drinks = None
add_in_price = None


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

    return sizes, add_in_price, base_drinks, add_ins_list

