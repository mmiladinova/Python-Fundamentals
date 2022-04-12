command = input()
contest_dict = dict()

while command != 'end of contests':
    (contest, password) = command.split(':')
    contest_dict[contest] = password
    command = input()

submission = input()
users_dict = dict()

while submission != 'end of submissions':
    (contest, password, username, points) = submission.split('=>')
    points = int(points)

    if contest in contest_dict and contest_dict[contest] == password:

        if username not in users_dict:
            users_dict[username] = dict()

        if contest not in users_dict[username]:
            users_dict[username][contest] = points
        else:
            if users_dict[username][contest] < points:
                users_dict[username][contest] = points

    submission = input()

max_points = 0
max_points_user = ''

for user in users_dict:
    total_points = sum(users_dict[user].values())
    if total_points > max_points:
        max_points = total_points
        max_points_user = user

print(f"Best candidate is {max_points_user} with total {max_points} points.")
print("Ranking:")
for user, value in sorted(users_dict.items()):
    print(user)
    for cont, point in sorted(users_dict[user].items(), key=lambda x: -x[1]):
        print(f'#  {cont} -> {point}')
