person = input()
phonebook = dict()

while "-" in person:
    person_info = person.split("-")
    name = person_info[0]
    phone = person_info[1]

    phonebook[name] = phone
    person = input()

n = int(person)

for num in range(n):
    search_name = input()

    if search_name in phonebook:
        print(f"{search_name} -> {phonebook[search_name]}")
    else:
        print(f"Contact {search_name} does not exist.")
