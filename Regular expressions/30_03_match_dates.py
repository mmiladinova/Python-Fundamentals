import re

input_text = input()

results = re.finditer(r"(?P<day>\d{2})(?P<separator>[./-])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})", input_text)

result_list = list()
for result in results:
    day = result.group("day")
    month = result.group("month")
    year = result.group("year")
    result_list.append(result.group())

    print(f"Day: {day}, Month: {month}, Year: {year}")
