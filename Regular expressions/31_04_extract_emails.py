import re

input_text = input()

# pattern = r'(^|(?<=\s))[a-zA-Z0-9]+([\.\-\_]?[a-zA-Z0-9]+)*@[a-zA-Z]+(-?[a-zA-Z]+)*(\.[a-zA-z]+-?[a-zA-Z]+)*(\b|(?=\s))'

pattern = r"(^|(?<=\s))(([a-zA-Z0-9]+)([\.\-_]?)([A-Za-z0-9]+)(@)([a-zA-Z]+([\.\-_][A-Za-z]+)+))(\b|(?=\s))"

result = re.finditer(pattern, input_text)

for mail in result:
    print(mail.group())