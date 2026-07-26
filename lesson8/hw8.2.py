def is_palindrome(text):
    clean_text = ""
    for char in text:
        if char.isalnum():
            char = char.lower()
            clean_text += char
    return clean_text == clean_text[::-1]
print (is_palindrome('A man, a plan, a canal: Panama'))
print (is_palindrome('0P'))
print (is_palindrome('a.'))
print (is_palindrome('aurora'))

