n = int(input())

hero_dict = dict()

for _ in range(n):
    hero_info = input().split()
    hero = hero_info[0]
    HP = int(hero_info[1])
    MP = int(hero_info[2])

    if HP <= 100 and MP <= 200:
        hero_dict[hero] = {'HP': HP, 'MP': MP}

command = input()

while command != "End":
    command_list = command.split(' - ')

    if command_list[0] == "CastSpell":
        hero_name = command_list[1]
        mp_needed = int(command_list[2])
        spell_name = command_list[3]

        if hero_dict[hero_name]['MP'] >= mp_needed:
            hero_dict[hero_name]['MP'] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {hero_dict[hero_name]['MP']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif command_list[0] == "TakeDamage":
        hero_name = command_list[1]
        damage = int(command_list[2])
        attacker = command_list[3]

        hero_dict[hero_name]['HP'] -= damage
        if hero_dict[hero_name]['HP'] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {hero_dict[hero_name]['HP']} HP left!")
        else:
            del hero_dict[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")

    elif command_list[0] == "Recharge":
        hero_name = command_list[1]
        amount = int(command_list[2])
        initial_mp = hero_dict[hero_name]['MP']
        hero_dict[hero_name]['MP'] += amount
        if hero_dict[hero_name]['MP'] > 200:
            hero_dict[hero_name]['MP'] = 200
            amount = 200 - initial_mp
        print(f"{hero_name} recharged for {amount} MP!")

    elif command_list[0] == "Heal":
        hero_name = command_list[1]
        amount = int(command_list[2])
        initial_hp = hero_dict[hero_name]['HP']
        hero_dict[hero_name]['HP'] += amount
        if hero_dict[hero_name]['HP'] > 100:
            hero_dict[hero_name]['HP'] = 100
            amount = 100 - initial_hp
        print(f"{hero_name} healed for {amount} HP!")

    command = input()

for hero, info in hero_dict.items():
    print(f"{hero}")
    for key, value in info.items():
        print(f"  {key}: {value}")
