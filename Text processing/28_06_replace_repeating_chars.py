input_str = input()

result_str = ''

for index in range(len(input_str) - 1):
    if index == 0:
        result_str = input_str[index]
    if input_str[index] != input_str[index + 1]:
        result_str += input_str[index + 1]

print(result_str)
