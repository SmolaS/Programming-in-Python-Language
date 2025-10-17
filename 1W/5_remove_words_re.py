import re

path = "D:\\Studia\\7 Semestr\\Python\\1W\\Katalog\\tekst1.txt"

with open(path, "r", encoding="utf-8") as file:
    text = file.read()

words_to_remove = ["egzamin", "i"]

result = text

for word in words_to_remove:
    pattern = "\\b" + word + "\\b"
    result = re.sub(pattern, "", result)

result = re.sub("\\s+", " ", result).strip()

print("OG tekst:", text)
print("Po usuwaniu:", result)