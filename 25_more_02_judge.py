command = input()
contest_dict = dict()
users_dict = dict()

while command != 'no more time':
    username, contest, points = command.split(' -> ')
    points = int(points)

    if contest not in contest_dict:
        contest_dict[contest] = dict()

    if username not in contest_dict[contest]:
        contest_dict[contest][username] = points
        if username not in users_dict:
            users_dict[username] = points
        else:
            users_dict[username] += points
    else:
        if contest_dict[contest][username] < points:
            users_dict[username] -= contest_dict[contest][username]
            users_dict[username] += points
            contest_dict[contest][username] = points

    command = input()

for contest, value in contest_dict.items():
    print(f"{contest}: {len(contest_dict[contest])} participants")
    br = 1
    for usr, point in sorted(value.items(), key=lambda x: (-x[1], x[0])):
        print(f"{br}. {usr} <::> {point}")
        br += 1


print(f"Individual standings:")
br = 0
for user, points in sorted(users_dict.items(), key=lambda x: (-x[1], x[0])):
    br += 1
    print(f"{br}. {user} -> {users_dict[user]}")
