def rate_plant(plants, plant, rating):
    if plant in plants:
        plants[plant]["ratings"].append(int(rating))
    else:
        print("error")


def update_plant(plants, plant, new_rarity):
    if plant in plants:
        plants[plant]["rarity"] = int(new_rarity)
    else:
        print("error")


def reset_plant(plants, plant):
    if plant in plants:
        plants[plant]["ratings"] = []
    else:
        print("error")


def exhibition(plants):
    print("Plants for the exhibition:")
    for plant, info in [("Arnoldii", plants["Arnoldii"]), ("Woodii", plants["Woodii"]), ("Welwitschia", plants["Welwitschia"])]:
        rarity = info["rarity"]
        ratings = info["ratings"]
        average_rating = sum(ratings) / len(ratings) if ratings else 0.00
        print(f"- {plant}; Rarity: {rarity}; Rating: {average_rating:.2f}")


number_of_plants = int(input())
plants = {}

for i in range(number_of_plants):
    plant, rarity = input().split('<->')
    if plant in plants:
        print('error')
    else:
        plants[plant] = {"rarity": int(rarity), "ratings": []}

command = input()

while command != "Exhibition":
    action, data = command.split(": ")
    plant, *args = data.split(" - ")

    if action == "Rate":
        rate_plant(plants, plant, *args)
    elif action == "Update":
        update_plant(plants, plant, *args)
    elif action == "Reset":
        reset_plant(plants, plant)

    command = input()

exhibition(plants)
