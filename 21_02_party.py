class Party:
    def __init__(self):
        self.people = list()


party_obj = Party()
command = input()

while command != 'End':
    party_obj.people.append(command)
    command = input()

people_result = ', '.join(party_obj.people)
print(f"Going: {people_result}")
print(f"Total: {len(party_obj.people)}")
