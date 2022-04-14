input_str = input()

result_str = ''
bomb = 0

for i in range(len(input_str)):
    if input_str[i] == '>':
        result_str += input_str[i]
        bomb += int(input_str[i + 1])
    elif input_str[i] != '>' and bomb > 0:
        bomb -= 1
    else:
        result_str += input_str[i]

print(result_str)
