path = "D:\\Studia\\7 Semestr\\Python\\1W\\Katalog\\tekst1.txt"

with open(path, "r", encoding="utf-8") as file:
    text = file.read()

words_to_remove = ["egzamin", "i"]

words = text.split()

filtered = []
for w in words:
    if w not in words_to_remove:
        filtered.append(w)

result = " ".join(filtered)

print("Tekst z pliku:")
print(text)
print("\nPo usuwaniu:")
print(result)
