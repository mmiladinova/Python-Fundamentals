product = input()
food_dict = {}

while product != 'statistics':
    product_list = product.split(": ")
    key = product_list[0]
    value = int(product_list[1])

    if key in food_dict:
        food_dict[key] += value
    else:
        food_dict[key] = value

    product = input()

print("Products in stock:")
for (key, value) in food_dict.items():
    print(f"{key}: {value}")
print(f"Total Products: {len(food_dict.keys())}")
print(f"Total Quantity: {sum(food_dict.values())}")
