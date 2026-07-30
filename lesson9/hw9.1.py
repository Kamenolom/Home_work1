def popular_words (text, words):
    text = text.lower()
    new_dict = {}
    for word in words:
        new_dict[word] = text.count(word)
    return new_dict
print(popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']))