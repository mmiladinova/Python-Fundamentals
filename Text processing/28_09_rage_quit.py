input_str = input().lower()

is_digit = False
word = ''
digit = ''
result_str = ''
symbols_list = list()

for index in range(len(input_str)):

    if input_str[index].isdigit():
        if index != (len(input_str) - 1) and input_str[index + 1].isdigit():
            digit += str(input_str[index])
        else:
            digit += str(input_str[index])
            is_digit = True
    else:
        word += input_str[index]
        if input_str[index] not in symbols_list:
            symbols_list.append(input_str[index])

    if is_digit:
        result_str += (word.upper() * int(digit))
        is_digit = False
        word = ''
        digit = ''

print(f"Unique symbols used: {len(symbols_list)}")
print(result_str)
