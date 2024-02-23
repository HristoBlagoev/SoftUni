class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammal = []
        self.fish = []
        self.bird = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammal.append(name)
            Zoo.__animals += 1
        elif species == 'fish':
            self.fish.append(name)
            Zoo.__animals += 1
        elif species == 'bird':
            self.bird.append(name)
            Zoo.__animals += 1

    def get_info(self, zoo_name, species1):
        if species1 == "mammal":
            return f"Mammals in {zoo_name}: {', '.join(self.mammal)}\nTotal animals: {Zoo.__animals}"
        elif species1 == "bird":
            return f"Birds in {zoo_name}: {', '.join(self.bird)}\nTotal animals: {Zoo.__animals}"
        elif species1 == "fish":
            return f"Fishes in {zoo_name}: {', '.join(self.fish)}\nTotal animals: {Zoo.__animals}"


name_of_zoo = input()
number_of_animals = int(input())
zoo = Zoo(name_of_zoo)

for _ in range(number_of_animals):
    command = input()
    current_command = command.split(" ")
    type_of_species = current_command[0]
    name_to_add = current_command[1]
    zoo.add_animal(type_of_species, name_to_add)

wanted_species = input()

print(zoo.get_info(name_of_zoo, wanted_species))