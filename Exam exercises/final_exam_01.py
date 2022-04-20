spell = input()

command = input()

while command != "Abracadabra":
    command_list = command.split()

    if command_list[0] == "Abjuration":
        spell = spell.upper()
        print(spell)

    elif command_list[0] == "Necromancy":
        spell = spell.lower()
        print(spell)

    elif command_list[0] == "Illusion":
        index = int(command_list[1])
        letter = command_list[2]

        if len(spell) > index >= 0:
            spell = spell[:index] + letter + spell[index + 1:]
            print("Done!")
        else:
            print(f"The spell was too weak.")

    elif command_list[0] == "Divination":
        first_sub = command_list[1]
        second_sub = command_list[2]

        spell = spell.replace(first_sub, second_sub)
        print(spell)

    elif command_list[0] == "Alteration":
        substring = command_list[1]

        spell = spell.replace(substring, '')
        print(spell)

    else:
        print(f"The spell did not work!")

    command = input()
