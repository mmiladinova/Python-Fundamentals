import re

input_text = input()

result = re.findall(r"\b[A-Z][a-z]+ [A-Z][a-z]+\b", input_text)

print(' '.join(result))