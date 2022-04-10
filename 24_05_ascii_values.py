char_list = input().split(", ")

ascii_dict = {ch: ord(ch) for ch in char_list}

print(ascii_dict)
