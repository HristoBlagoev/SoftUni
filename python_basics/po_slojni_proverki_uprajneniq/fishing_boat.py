budget = int(input())
season = input()
qty_fishermen = int(input())
price = 0
difference = 0

if season == 'Spring':
    price = 3000
elif season == 'Summer' or season == 'Autumn':
    price = 4200
elif season == 'Winter':
    price = 2600
elif 6 >= qty_fishermen:
    price *= 0.90
elif 7 <= qty_fishermen <= 11:
    price *= 0.85
elif 12 <= qty_fishermen:
    price *= 0.75
if qty_fishermen % 2 == 0 and season != "Autumn":
    price *= 0.95
difference = abs(price - budget)

if budget >= price:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")
