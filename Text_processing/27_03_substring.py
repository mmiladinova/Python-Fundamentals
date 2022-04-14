search_word = input()
text = input()

while search_word in text:
    text = text.replace(search_word, '')

print(text)
