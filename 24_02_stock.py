


food_list = input().split(" ")
search_products = input().split(" ")
food_dict = dict()

for x in range(0, len(food_list), 2):
    key = food_list[x]
    value = food_list[x + 1]
    food_dict[key] = int(value)

for product in search_products:
    if product in food_dict.keys():
        print(f"We have {food_dict.get(product)} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
