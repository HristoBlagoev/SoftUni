team = input()
type_of_souvenir = input()
qty_of_purchased_souvenirs = int(input())
price = 0

if team == 'Argentina':
    if type_of_souvenir == 'flags':
        price = 3.25
    elif type_of_souvenir == 'caps':
        price = 7.20
    elif type_of_souvenir == 'posters':
        price = 5.10
    elif type_of_souvenir == 'stickers':
        price = 1.25
elif team == 'Brazil':
    if type_of_souvenir == 'flags':
        price = 4.20
    elif type_of_souvenir == 'caps':
        price = 8.50
    elif type_of_souvenir == 'posters':
        price = 5.35
    elif type_of_souvenir == 'stickers':
        price = 1.20
elif team == 'Croatia':
    if type_of_souvenir == 'flags':
        price = 2.75
    elif type_of_souvenir == 'caps':
        price = 6.90
    elif type_of_souvenir == 'posters':
        price = 4.95
    elif type_of_souvenir == 'stickers':
        price = 1.10
elif team == 'Denmark':
    if type_of_souvenir == 'flags':
        price = 3.10
    elif type_of_souvenir == 'caps':
        price = 6.50
    elif type_of_souvenir == 'posters':
        price = 4.80
    elif type_of_souvenir == 'stickers':
        price = 0.90
final_price = price * qty_of_purchased_souvenirs

if team != 'Argentina' and team != 'Brazil' and team != 'Croatia' and team != 'Denmark':
    print('Invalid country!')
elif type_of_souvenir != 'flags' and type_of_souvenir != 'caps' \
        and type_of_souvenir != 'posters' and type_of_souvenir != 'stickers':
    print("Invalid stock!")
else:
    print(f'Pepi bought {qty_of_purchased_souvenirs} {type_of_souvenir} of {team} for {final_price:.2f} lv.')
