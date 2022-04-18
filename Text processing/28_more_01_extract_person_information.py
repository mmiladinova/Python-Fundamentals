n = int(input())

for _ in range(n):
    input_list = input().split()
    name = ''
    age = 0

    for word in input_list:
        if "@" and "|" in word:
            first_index = word.index("@")
            second_index = word.index("|")
            name = word[first_index + 1:second_index]
        if "#" and "*" in word:
            first_index = word.index("#")
            second_index = word.index("*")
            age = word[first_index + 1:second_index]

    print(f"{name} is {age} years old.")
