encrypted_msg = input()

command = input()

while command != 'Decode':
    command_list = command.split('|')

    if 'Move' in command_list:
        move_num = int(command_list[1])
        move = encrypted_msg[:move_num]
        encrypted_msg = encrypted_msg[move_num:] + move

    elif 'Insert' in command_list:
        index = int(command_list[1])
        value = command_list[2]
        encrypted_msg = encrypted_msg[:index] + value + encrypted_msg[index:]

    elif 'ChangeAll' in command_list:
        substring = command_list[1]
        replacement = command_list[2]
        encrypted_msg = encrypted_msg.replace(substring, replacement)

    command = input()
print(f'The decrypted message is: {encrypted_msg}')
