from string import ascii_lowercase

input_list = input().split()

total_sum = 0

for word in input_list:
    suma = 0
    number = [num for num in word if num.isdigit()]
    number = ''.join(number)

    for i in range(len(word)):
        if word[i].isalpha():
            position = ascii_lowercase.index(word[i].lower()) + 1
            if i == 0:
                if word[i].isupper():
                    suma += int(number) / position
                elif word[i].islower():
                    suma += int(number) * position

            elif i == len(word) - 1:
                last_index = len(word) - 1
                if word[last_index].isupper():
                    suma -= position
                elif word[last_index].islower():
                    suma += position

    total_sum += suma
print(f"{total_sum:.2f}")
