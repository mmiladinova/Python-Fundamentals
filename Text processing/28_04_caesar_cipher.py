input_str = input()

result_str = [chr(ord(i) + 3) for i in input_str]

print(''.join(result_str))
