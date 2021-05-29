import os
import json
from Dependencies import LabelPrinting

#class to Store Imported Menu Info
class Menu:
    def __init__(self, menu_base_drinks, menu_add_ins, menu_add_in_price, menu_sizes, menu_sodas):
        self.base_drinks = menu_base_drinks
        self.add_ins = menu_add_ins
        self.add_in_price = menu_add_in_price
        self.sizes = menu_sizes
        self.sodas = menu_sodas

#class Representing Customized Order Items
class OrderItem:
    def __init__(self, base_item, size, soda, item_add_ins=None):
        if item_add_ins is None:
            add_ins = []
        self.base_item = base_item
        self.size = size
        self.soda = soda
        self.add_ins = item_add_ins
        extra_add_ins = []
        for add_in in item_add_ins:
            if not add_in in menu.base_drinks[base_item]:
                extra_add_ins.append(add_in)
        self.extra_add_ins = extra_add_ins
        self.price = float(round_float(menu.sizes[size] + (len(extra_add_ins) * menu.add_in_price)))

    def __str__(self):
        if self.extra_add_ins:
            return f'{self.size} {self.soda}, {self.base_item} + {", ".join(self.extra_add_ins)}'
        else:
            return f'{self.size} {self.soda}, {self.base_item}'
    
    def summary(self):
        summary = f"{self.size}\n{self.base_item}"
        for add_in in self.add_ins:
            summary += f"\n+{add_in}"
        summary += f"\n{self.price}"
        return summary

class ActiveOrder:
    def __init__(self, listbox):
        self.current_item_base = None
        self.list_index = None
        self.listbox = listbox
        self.order_items = []
    
    def add_to_order(self, item):
        self.order_items.append(item)
        self.listbox.delete(0, "end")
        for list_item in self.order_items:
            self.listbox.insert("end", list_item)

    def remove_from_order(self, item):
        self.order_items.remove(item)
        self.listbox.delete(0, "end")
        for list_item in self.order_items:
            self.listbox.insert("end", list_item)
    
    def order_summary(self):
        order_summary_list = []
        for order_item in self.order_items:
            order_summary_list.append((order_item, order_item.price))
        return order_summary_list

    def total(self):
        order_total = 0
        for item in self.order_items:
            order_total += item.price
        return round_float(order_total)

def round_float(float_value):
    return format(float_value, '.2f')

#Importing Menu Information and converting to dictionaries
def menu_import():
    with open("menu.json") as menu_file:
        json_data = json.load(menu_file)
        sizes = json_data["prices"]["sizes"]
        base_drinks = json_data["base drinks"]
        add_in_price = json_data["prices"]["Add-In"]
        sodas = json_data["sodas"]

    #Temporary Add-In List
    add_ins_list = set()
    for drink in base_drinks.values():
        add_ins_list |= set(drink)
    add_ins_list = sorted(list(add_ins_list))

    return Menu(base_drinks, add_ins_list, add_in_price, sizes, sodas)

menu = menu_import()