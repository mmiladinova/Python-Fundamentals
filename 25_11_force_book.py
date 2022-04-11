def create_force_side(side, user, force_side_users):
    condition = [current_side for current_side in force_side_users if user in force_side_users[current_side]]
    if len(condition) == 0:
        if side not in force_side_users.keys():
            force_side_users[side] = [user]
        else:
            force_side_users[side].append(user)

    return force_side_users


def create_force_users(user, side, force_side_users):
    for curr_side in force_side_users:
        if user in force_side_users[curr_side]:
            if len(force_side_users[curr_side]) > 1:
                force_side_users[curr_side].pop(user)
                break
            else:
                del force_side_users[curr_side]
                break

    if side in force_side_users:
        force_side_users[side].append(user)
    else:
        force_side_users[side] = [user]

    print(f"{user} joins the {side} side!")
    return force_side_users


def force_book():
    command = input()
    force_side_users = {}

    while command != 'Lumpawaroo':
        if ' | ' in command:
            command = command.split(' | ')
            side = command[0]
            user = command[1]
            create_force_side(side, user, force_side_users)
        elif ' -> ' in command:
            command = command.split(' -> ')
            side = command[1]
            user = command[0]
            create_force_users(user, side, force_side_users)

        command = input()

    for key in force_side_users:
        print(f"Side: {key}, Members: {len(force_side_users[key])}")
        for curr_user in force_side_users[key]:
            print(f"! {curr_user}")


force_book()
