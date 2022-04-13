n = int(input())
synonym_dict = {}

for count in range(n):
    word = input()
    synonym = input()

    if word not in synonym_dict:
        synonym_dict[word] = list()

    synonym_dict[word].append(synonym)

for key, value in synonym_dict.items():
    print(f"{key} - ", end="")
    synonym_list = ", ".join(value)
    print(f"{synonym_list}")
