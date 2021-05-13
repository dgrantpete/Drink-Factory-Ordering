import os
import json
from Dependencies import LabelPrinting, GUI

class OrderItem:
    def __init__(self, base_item, size, add_ins=None):
        if add_ins is None:
            add_ins = []
        self.base_item = base_item
        self.size = size
        self.add_ins = add_ins
        self.price = prices[size] + (len(add_ins) * prices["Add-In"])

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
    