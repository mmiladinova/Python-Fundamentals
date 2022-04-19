import re

input_text = input()

total_money = 0
furniture_list = list()

while input_text != "Purchase":

    pattern = r'>>([a-zA-Z]+)<<([0-9]+|[0-9]+\.[0-9]+)!([0-9]+)'

    result = re.match(pattern, input_text)

    if result is not None:
        r_furniture = result[1]
        r_price = float(result[2])
        r_quantity = float(result[3])

        total_money += r_price * r_quantity
        furniture_list.append(r_furniture)

    input_text = input()

print("Bought furniture:")
for item in furniture_list:
    print(item)
print(f"Total money spend: {total_money:.2f}")
