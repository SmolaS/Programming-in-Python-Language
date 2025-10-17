import os

path = "D:\\Studia\\7 Semestr\\Python\\1W\\Katalog"

import os

def wypisz_pliki(path):
    for entry in os.scandir(path):
        if entry.is_file():
            print(entry.path)
        elif entry.is_dir():
            wypisz_pliki(entry.path)

wypisz_pliki(path)