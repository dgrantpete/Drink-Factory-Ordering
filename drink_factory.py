import os
import json
from Dependencies import LabelPrinting
from Dependencies.GUI import root, add_grid_item, add_sizes, add_add_ins, add_check_state, return_add_ins, drink_edit

class OrderItem:
    def __init__(self, base_item, size, add_ins=None):
        if add_ins is None:
            add_ins = []
        self.base_item = base_item
        self.size = size
        self.add_ins = add_ins
        self.price = prices["sizes"][size] + (len(add_ins) * prices["Add-In"])

    def __str__(self):
        return f'{self.size} {self.base_item} +{", ".join(self.add_ins)} for {self.price}'
    
    def summary(self):
        summary = f"{self.size}\n{self.base_item}"
        for add_in in self.add_ins:
            summary += f"\n+{add_in}"
        return summary

#Importing Menu Information and converting to dictionaries
with open("menu.json") as menu_file:
    json_data = json.load(menu_file)
    prices = json_data["prices"]
    base_drinks = json_data["base drinks"]

#Temporary Add-In List
add_ins_list = set()
for drink in base_drinks.values():
    add_ins_list |= set(drink)
add_ins_list = sorted(list(add_ins_list))

#Adding Menu Buttons for Drinks
for drink in base_drinks:
    add_grid_item(drink)

#Adding Drink Sizes to Edit Menu
add_sizes(prices["sizes"])

#Adding Add-Ins to Edit Menu
add_add_ins(add_ins_list)

test_order = OrderItem("Ry-Guy", "16oz", ["Cherry", "Blackberry"])

drink_edit(test_order)

root.mainloop()
