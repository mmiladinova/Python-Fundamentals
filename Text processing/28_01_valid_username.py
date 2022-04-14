import string

usernames = input().split(', ')
valid_symbols = string.digits + string.ascii_letters + '-' + '_'


for username in usernames:
    is_valid = True
    if len(username) < 3 or len(username) > 16:
        is_valid = False
    for ch in username:
        if ch not in valid_symbols:
            is_valid = False
            break

    if is_valid:
        print(username)
