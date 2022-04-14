input_text = input()

emoticons = [(input_text[x] + input_text[x + 1]) for x in range(len(input_text)) if input_text[x] == ':']

print('\n'.join(emoticons))
