budget_movie = float(input())
number_of_people = int(input())
dress_per_person = float(input())
difference = 0

decor_price = budget_movie * 0.10
dress_price = dress_per_person * number_of_people

if number_of_people > 150:
    dress_price *= 0.90

total_price_movie = decor_price + dress_price
difference = abs(total_price_movie - budget_movie)

if total_price_movie > budget_movie:
    print('Not enough money!')
    print(f'Wingard needs {difference:.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {difference:.2f} leva left.')