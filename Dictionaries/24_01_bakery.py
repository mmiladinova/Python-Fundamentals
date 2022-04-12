food = input().split(" ")
food_dict = dict()

for x in range(0, len(food), 2):
    key = food[x]
    value = int(food[x + 1])
    food_dict[key] = value

print(food_dict)