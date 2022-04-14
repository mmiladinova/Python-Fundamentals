word = input()

while word != 'end':
    reversed_word = ''
    for ch in reversed(word):
        reversed_word += ch

    print(f"{word} = {reversed_word}")
    word = input()
