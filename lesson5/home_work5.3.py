import string
import keyword
text = input("Enter in text: " )
is_valid = True
if text[0].isdigit():
    is_valid = False
for symbol in text:
    if symbol.isupper():
        is_valid = False
if " " in text:
    is_valid = False
for symbol in text:
    if symbol in string.punctuation and symbol != "_":
        is_valid = False
if text in keyword.kwlist:
    is_valid = False
if "__" in text:
    is_valid = False
print(is_valid)
