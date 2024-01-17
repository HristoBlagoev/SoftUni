type_of_flower = input()
qty_of_flowers = int(input())
budget = int(input())
price = 0
difference = 0

if type_of_flower == 'Roses':
    price = qty_of_flowers * 5
    if 80 < qty_of_flowers:
        price *= 0.90
elif type_of_flower == 'Dahlias':
    price = qty_of_flowers * 3.80
    if 90 < qty_of_flowers:
        price *= 0.85
elif type_of_flower == 'Tulips':
    price = qty_of_flowers * 2.8
    if 80 < qty_of_flowers:
        price *= 0.85
elif type_of_flower == 'Narcissus':
    price = qty_of_flowers * 3
    if 120 > qty_of_flowers:
        price *= 1.15
elif type_of_flower == 'Gladiolus':
    price = qty_of_flowers * 2.50
    if 80 > qty_of_flowers:
        price *= 1.20
difference = abs(price - budget)

if budget >= price:
    print(f"Hey, you have a great garden with {qty_of_flowers} {type_of_flower} and {difference:.2f} leva left.")
elif budget < price:
    print(f'Not enough money, you need {difference:.2f} leva more.')