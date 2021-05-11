import os
import pathlib

def print_label(data):

    with open("label.txt", 'w') as label_file:
        label_file.write(data)

    os.startfile("label.txt", 'print')
    