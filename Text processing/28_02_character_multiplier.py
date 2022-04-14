str1, str2 = input().split()

total_sum = 0

if len(str1) > len(str2):
    max_word = str1
    min_word = str2
else:
    max_word = str2
    min_word = str1

for x in range(len(max_word)):
    if x < len(min_word):
        total_sum += ord(min_word[x]) * ord(max_word[x])
    else:
        total_sum += ord(max_word[x])

print(total_sum)
