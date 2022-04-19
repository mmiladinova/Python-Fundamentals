import re
input_text = input()
res_list = []
while input_text:

    pattern = r'(www\.)([a-zA-Z0-9-]+)((\.[a-z]+)+)'

    result = re.finditer(pattern, input_text)
    if result is not None:
        for item in result:
            res_list.append(item.group())
            print(item.group())

    input_text = input()