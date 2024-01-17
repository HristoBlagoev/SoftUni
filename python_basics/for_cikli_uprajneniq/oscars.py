actor_name = input()
academy_points = float(input())
qty_judges = int(input())

total_points = academy_points

for judges in range(qty_judges):
    name_evaluator = input()
    points = float(input())

    total_points += len(name_evaluator) * points / 2

    if total_points > 1250.5:
        break

difference = 1250.5 - total_points

if total_points > 1250.5:
    print(f'Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!')
else:
    print(f'Sorry, {actor_name} you need {difference:.1f} more!')
