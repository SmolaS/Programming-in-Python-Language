def is_palindrome(text):
    text = text.lower()
    text = text.replace(" ", "")
    return text == text[::-1]
s = "Kajak"
print(is_palindrome(s))