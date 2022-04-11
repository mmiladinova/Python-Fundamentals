command = input()
languages_dict = dict()
submission = dict()

while command != 'exam finished':
    command = command.split('-')
    username = command[0]

    if 'banned' in command:
        for key, value in languages_dict.items():
            for in_key, in_val in value.items():
                if username == in_key:
                    languages_dict[key].pop(in_key)
                    break

    else:
        language = command[1]
        points = int(command[2])

        if language not in submission:
            submission[language] = 0
        submission[language] += 1

        # if there is no such user - create it
        if language not in languages_dict:
            languages_dict[language] = dict()
        #check if user is already created, if there is no user len = 0 and create user
        condition = [lang for lang in languages_dict if username in languages_dict[language]]
        if len(condition) == 0:
            languages_dict[language][username] = points
        #check if there is submission with lower points
        for key, value in languages_dict.items():
            for in_key, in_val in value.items():
                if in_key == username and key == language:
                    if languages_dict[key][in_key] < points:
                        languages_dict[key][in_key] = points

    command = input()

print(f"Results:")
for key, value in languages_dict.items():
    for in_key, in_value in value.items():
        print(f"{in_key} | {in_value}")
print("Submissions:")
for key, value in submission.items():
    print(f"{key} - {value}")
