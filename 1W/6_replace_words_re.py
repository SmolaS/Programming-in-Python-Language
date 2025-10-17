import re

path = "D:\\Studia\\7 Semestr\\Python\\1W\\Katalog\\tekst2.txt"

with open(path, "r", encoding="utf-8") as file:
    text = file.read()
    
replace = {"CODa": "BFa", "egzamin": "wolne"}

result = text

for word, new_word in replace.items():
    pattern = "\\b" + word + "\\b"
    result = re.sub(pattern, new_word, result)

print("OG tekst:", text)
print("Po zastąpieniu:", result)
