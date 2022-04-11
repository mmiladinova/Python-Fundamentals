command = input()
resources_dict = {}

while command != "stop":
    resource = command
    quantity = int(input())

    if resource not in resources_dict:
        resources_dict[resource] = 0

    resources_dict[resource] += quantity
    command = input()

for key, value in resources_dict.items():
    print(f"{key} -> {value}")
