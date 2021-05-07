import os
import pathlib

def print_label(data):
    label = pathlib.Path(__file__).cwd()/"label.txt"

    os.remove(label)

    with open(label, 'w') as label_file:
        label_file.write(data)

    os.startfile(label, 'print')