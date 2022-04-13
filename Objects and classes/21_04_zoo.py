class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = list()
        self.fishes = list()
        self.birds = list()

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        if species == 'mammal':
            print(f"Mammals in {self.name}: {', '.join(zoo.mammals)}")
            print(f"Total animals: {Zoo.__animals}")
        elif species == 'fish':
            print(f"Fishes in {self.name}: {', '.join(zoo.fishes)}")
            print(f"Total animals: {Zoo.__animals}")
        elif species == 'bird':
            print(f"Birds in {self.name}: {', '.join(zoo.birds)}")
            print(f"Total animals: {Zoo.__animals}")


zoo_name = input()
zoo = Zoo(zoo_name)
n = int(input())

for num in range(n):
    animal_info = input().split(' ')
    animal_species = animal_info[0]
    animal_name = animal_info[1]

    zoo.add_animal(animal_species, animal_name)

chosen_species = input()
zoo.get_info(chosen_species)
