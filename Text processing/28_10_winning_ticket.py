def find_largest_string(text):
    current_max_num = 0
    special_char = ''

    for ch in text:
        if ch != special_char:
            if current_max_num >= 6:
                break
            current_max_num = 1
            special_char = ch
        else:
            current_max_num += 1

    return current_max_num, special_char


ticket_list = input().split(', ')

for ticket in ticket_list:
    ticket = ticket.strip()
    string1 = ticket[:10]
    string2 = ticket[10:]

    num1, special_char1 = find_largest_string(string1)
    num2, special_char2 = find_largest_string(string2)
    num = min(num1, num2)

    if len(ticket) != 20:
        print("invalid ticket")
    elif ticket[0] * 20 == ticket and ticket[0] in '@#$^':
        print(f'ticket "{ticket}" - {num}{special_char1} Jackpot!')
    elif num <= 5 or special_char1 not in '@#$^':
        print(f'ticket "{ticket}" - no match')
    else:
        print(f'ticket "{ticket}" - {num}{special_char1}')
