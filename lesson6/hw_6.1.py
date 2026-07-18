import string
is_valid = True
text = input("Enter the 2 letters: ")
letters = text.split("-")
if len(letters) != 2:
    is_valid = False
if is_valid:
    start = letters[0]
    end = letters[1]
    if start not in string.ascii_letters or end not in string.ascii_letters:
        is_valid = False
if is_valid:
    start_index = string.ascii_letters.index(start)
    end_index = string.ascii_letters.index(end)
    if start_index > end_index:
        is_valid = False
if is_valid:
    result = string.ascii_letters[start_index : end_index + 1]
    print(result)
