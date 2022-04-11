n = int(input())
registered_names_dict = {}

for x in range(n):
    command = input().split()
    name = command[1]
    if 'register' in command:
        number = command[2]
        if name in registered_names_dict:
            print(f"ERROR: already registered with plate number {number}")
        else:
            registered_names_dict[name] = number
            print(f"{name} registered {number} successfully")
    elif 'unregister' in command:
        if name not in registered_names_dict:
            print(f"ERROR: user {name} not found")
        else:
            del registered_names_dict[name]
            print(f"{name} unregistered successfully")

for name, reg_num in registered_names_dict.items():
    print(f"{name} => {reg_num}")
