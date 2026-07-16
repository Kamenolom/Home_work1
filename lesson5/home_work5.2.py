import string
text = input("Enter a text: ")
clean_text = ""
for symbol in text:
    if symbol not in string.punctuation:
        clean_text += symbol
words = clean_text.split()
new_words = []
for word in words:
    new_words.append(word.capitalize())
words_capitalized = "".join(new_words)
if len(words_capitalized) > 140:
    words_capitalized = words_capitalized[:140]
hashtag = "#" + words_capitalized
print(hashtag)
