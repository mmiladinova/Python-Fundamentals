import re

input_text = input()

result = re.findall(r'\b_[a-zA-Z0-9]+\b', input_text)

result_list = list()

for word in result:
    result_list.append(word[1:])

print(','.join(result_list))
