budget = float(input())
season = input()
spent_money = 0
destination = ''
type_of_holiday = ''

if budget <=100:
    destination = 'Bulgaria'
    if season == 'summer':
        spent_money = budget * 0.30
        type_of_holiday = 'Camp'
    if season == 'winter':
        spent_money = budget * 0.70
        type_of_holiday = 'Hotel'
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        spent_money = budget * 0.40
        type_of_holiday = 'Camp'
    if season == 'winter':
        spent_money = budget * 0.80
        type_of_holiday = 'Hotel'
elif budget > 1000:
    destination = 'Europe'
    if destination == 'Europe':
        spent_money = budget * 0.90
        type_of_holiday = 'Hotel'

print(f'Somewhere in {destination}')
print(f'{type_of_holiday} - {spent_money:.2f}')