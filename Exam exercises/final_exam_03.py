command = input()

heroes_dict = dict()

while command != "End":
    command_list = command.split()

    if command_list[0] == "Enroll":
        hero = command_list[1]
        if hero in heroes_dict:
            print(f"{hero} is already enrolled.")
        else:
            heroes_dict[hero] = list()

    if command_list[0] == "Learn":
        hero = command_list[1]
        spell = command_list[2]

        if hero in heroes_dict:
            if spell not in heroes_dict[hero]:
                heroes_dict[hero].append(spell)
            else:
                print(f"{hero} has already learnt {spell}.")
        else:
            print(f"{hero} doesn't exist.")

    if command_list[0] == "Unlearn":
        hero = command_list[1]
        spell = command_list[2]

        if hero in heroes_dict:
            if spell not in heroes_dict[hero]:
                print(f"{hero} doesn't know {spell}.")
            else:
                heroes_dict[hero].remove(spell)
        else:
            print(f"{hero} doesn't exist.")

    command = input()

print("Heroes:")
for hero in heroes_dict:
    print(f"== {hero}: ", end='')
    print(', '.join(heroes_dict[hero]))


