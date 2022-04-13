input_string = input()
char_dict = dict()

for ch in input_string:
    if ch != ' ':
        if ch not in char_dict:
            char_dict[ch] = 0

        char_dict[ch] += 1

for key, value in char_dict.items():
    print(f"{key} -> {value}")
