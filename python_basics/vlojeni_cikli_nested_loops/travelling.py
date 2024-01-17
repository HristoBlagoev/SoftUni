destination = input()

while destination != 'End':
    min_budget = float(input())
    needed_money = 0

    while min_budget > needed_money:
        earned_money = float(input())
        needed_money += earned_money

    print(f'Going to {destination}!')

    destination = input()