first_match = input()
second_match = input()
third_match = input()
team_wins = 0
team_loses = 0
draws = 0
# executed_goals_first_match = int(first_match[0], second_match[0], third_match[0])
# received_goals_first_match = int(first_match[3], second_match[3], third_match[3])

for executed in range(1, int(first_match[1]) + 1):
    for received in range(1, int(first_match[3]) + 1):
        if executed > received:
            team_wins += 1
        elif executed < received:
            team_loses += 1
        else:
            draws += 1

for executed in range(1, int(second_match[1]) + 1):
    for received in range(1, int(second_match[3]) + 1):
        if executed > received:
            team_wins += 1
        elif executed < received:
            team_loses += 1
        else:
            draws += 1

for executed in range(1, int(third_match[1]) + 1):
    for received in range(1, int(third_match[3]) + 1):
        if executed > received:
            team_wins += 1
        elif executed < received:
            team_loses += 1
        else:
            draws += 1

print(f"Team won {team_wins} games.")
print(f"Team lost {team_loses} games.")
print(f" Drawn games: {draws}")
