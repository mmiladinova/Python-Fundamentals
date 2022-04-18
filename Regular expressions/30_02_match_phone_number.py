import re

input_text = input()

result = re.finditer(r"\+359([ |-])2\1\d{3}\1\d{4}\b", input_text)

output = list()
for item in result:
    output.append(item.group())

print(", ".join(output))
