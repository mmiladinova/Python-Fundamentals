import re

input_text = input()
pattern = input()

result = re.findall(rf'\b{pattern}\b', input_text, re.IGNORECASE)

print(len(result))
