days_of_stay = int(input())
type_of_room = input()
review = input()
nights_of_stay = days_of_stay - 1
price = 0

if type_of_room == 'room for one person':
    price = nights_of_stay * 18.00
elif type_of_room == 'apartment':
    price = nights_of_stay * 25
    if 10 > nights_of_stay:
        price *= 0.70
    if 10 <= nights_of_stay < 15:
        price *= 0.65
    if 15 < nights_of_stay:
        price *= 0.50
elif type_of_room == 'president apartment':
    price = nights_of_stay * 35
    if 10 > nights_of_stay:
        price *= 0.90
    if 10 <= nights_of_stay < 15:
        price *= 0.85
    if 15 < nights_of_stay:
        price *= 0.80
if review == 'positive':
    price *= 1.25
elif review == 'negative':
    price *= 0.90

print(f'{price:.02f}')