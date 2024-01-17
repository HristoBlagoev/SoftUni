from math import ceil, floor

price_tennis_rocket = float(input())
qty_of_tennis_rocket = int(input())
qty_of_trainers = int(input())
price_trainers = price_tennis_rocket / 6

total_price_tennis_rockets = price_tennis_rocket * qty_of_tennis_rocket
total_price_trainers = price_trainers * qty_of_trainers
other_equipment = (total_price_trainers + total_price_tennis_rockets) * 0.20
total_price = total_price_trainers + total_price_tennis_rockets + other_equipment
price_djokovic = floor(total_price / 8)
price_sponsors = ceil(total_price * 7 / 8)

print(f'Price to be paid by Djokovic {price_djokovic}')
print(f'Price to be paid by sponsors {price_sponsors}')