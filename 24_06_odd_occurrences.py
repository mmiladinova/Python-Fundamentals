input_list = (input().lower()).split(" ")
dictionary = dict()

for word in input_list:
    if word not in dictionary:
        dictionary[word] = 0

    dictionary[word] += 1

for key, value in dictionary.items():
    if value % 2 != 0:
        print(key, end=" ")
