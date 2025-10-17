import os

path = "D:\\Studia\\7 Semestr\\Python\\1W\\Katalog"
i = 0

for x in os.scandir(path):
    if x.is_file():
        i += 1

print("Liczba plików w katalogu:", i)