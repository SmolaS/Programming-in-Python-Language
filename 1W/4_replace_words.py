path = "D:\\Studia\\7 Semestr\\Python\\1W\\Katalog\\tekst2.txt"

with open(path, "r", encoding="utf-8") as file:
    text = file.read()

replace_dict = {"CODa": "BFa", "egzamin": "wolne"}

words = text.split()

filtered = []
for w in words:
    if w in replace_dict:
        filtered.append(replace_dict[w])
    else:
        filtered.append(w)

result = " ".join(filtered)

print("OG teskt:", text)
print("Po zastepieniu:", result)