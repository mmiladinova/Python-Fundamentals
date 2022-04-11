def print_products(items_dict):
    for item, info in items_dict.items():
        total_price = info['price'] * info['quantity']
        print(f"{item} -> {total_price:.2f}")


def fill_dict(input_command):
    product_dict = dict()
    while input_command != 'buy':
        input_command = input_command.split(' ')
        name = input_command[0]
        price = float(input_command[1])
        quantity = int(input_command[2])
        if name in product_dict:
            product_dict[name]['price'] = price
            product_dict[name]['quantity'] += quantity
        else:
            product_dict[name] = {'price': price, 'quantity': quantity}

        input_command = input()
    return product_dict


input_list = input()

print_products(fill_dict(input_list))
