def print_result(items, junk, spec_item):
    print(f"{spec_item} obtained!")
    print(f"shards: {items['shards']}")
    print(f"fragments: {items['fragments']}")
    print(f"motes: {items['motes']}")

    for key, value in junk.items():
        print(f"{key}: {value}")


input_list = (input().lower()).split(" ")
items_dict = {'shards': 0, 'fragments': 0, 'motes': 0}
junk_dict = dict()
is_finished = False
special_item = ''

while not is_finished:

    for item in range(0, len(input_list), 2):
        current_item = input_list[item + 1]
        quantity = int(input_list[item])

        if current_item in ['motes', 'shards', 'fragments']:
            items_dict[current_item] += quantity
        else:
            if current_item not in junk_dict:
                junk_dict[current_item] = 0
            junk_dict[current_item] += quantity

        if current_item in items_dict:
            if items_dict[current_item] >= 250:
                items_dict[current_item] -= 250
                if current_item == 'shards':
                    special_item = 'Shadowmourne'
                elif current_item == 'fragments':
                    special_item = 'Valanyr'
                elif current_item == 'motes':
                    special_item = 'Dragonwrath'
                is_finished = True
                break

    if not is_finished:
        input_list = (input().lower()).split(" ")

print_result(items_dict, junk_dict, special_item)
