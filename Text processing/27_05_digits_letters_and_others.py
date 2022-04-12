input_string = input()

digits = ''
letters = ''
others = ''

for ch in input_string:
    if ch.isalnum():
        if ch.isdigit():
            digits += ch
        else:
            letters += ch
    else:
        others += ch
    # if ch.isdigit():
    #     digits += ch
    # elif ch.isalpha():
    #     letters += ch
    # else:
    #     others += ch

print(digits)
print(letters)
print(others)