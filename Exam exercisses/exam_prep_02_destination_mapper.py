import re

destinations = input()

dest_list = list()

travel_points = 0

pattern = r'(?<=(=|/))([A-Z][a-zA-Z]{2,})(?=\1)'

result = re.finditer(pattern, destinations)

for item in result:
    dest_list.append(item.group())
    travel_points += len(item.group())

dest = ', '.join(dest_list)
print(f"Destinations: {dest}")
print(f'Travel Points: {travel_points}')
