text = input().split()

result_str = ''
for word in text:
    result_str += word * len(word)

print(result_str)