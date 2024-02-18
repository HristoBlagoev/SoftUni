energy = int(input())
won_battle_counter = 0
if_enough_energy = True

command = input()

while command != "End of battle":
    current_distance = int(command)
    if energy - current_distance < 0:
        if_enough_energy = False
        break

    energy -= current_distance
    won_battle_counter += 1

    if won_battle_counter % 3 == 0:
        energy += won_battle_counter

    command = input()

if if_enough_energy:
    print(f"Won battles: {won_battle_counter}. Energy left: {energy}")
else:
    print(f"Not enough energy! Game ends with {won_battle_counter} won battles and {energy} energy")
