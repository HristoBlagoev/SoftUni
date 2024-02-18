needed_experience = float(input())
number_of_battles = int(input())

experience_counter = 0
battles_counter = 0
is_tank_unlocked = False

for battle in range(1, number_of_battles + 1):
    current_battle = float(input())
    battles_counter += 1
    experience_counter += current_battle
    if battles_counter % 3 == 0:
        experience_counter +=  + current_battle * 0.15

    if battles_counter % 5 == 0:
        experience_counter -= current_battle * 0.10

    if battles_counter % (3*5) == 0:
        experience_counter += current_battle * 0.05

    if experience_counter >= needed_experience:
        is_tank_unlocked = True
        break


difference = abs(experience_counter - needed_experience)

if is_tank_unlocked:
    print(f"Player successfully collected his needed experience for {battles_counter} battles.")
else:
    print(f"Player was not able to collect the needed experience, {difference:.2f} more needed.")
