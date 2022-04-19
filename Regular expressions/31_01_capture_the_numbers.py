import re

while True:
    input_text = input()

    if not input_text:
        break

    result = re.findall(r"\d+", input_text)

    if len(result) > 0:
        print(' '.join(result), end=' ')
