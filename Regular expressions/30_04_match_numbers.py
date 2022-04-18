import re

input_text = input()

expression = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.[0-9]+)?($|(?=\s))"
results = re.finditer(expression, input_text)

result_list = list()

for match in results:
    result_list.append(match.group())

print(" ".join(result_list))
