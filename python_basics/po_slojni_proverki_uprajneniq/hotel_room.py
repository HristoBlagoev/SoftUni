month = input()
qty_of_nights = int(input())
price_for_studio = 0
price_for_apartment = 0

if month == 'May' or month == 'October':
    price_for_studio = qty_of_nights * 50.00
    if 14 < qty_of_nights:
        price_for_studio *= 0.70
    elif 7 < qty_of_nights:
        price_for_studio *= 0.95
    price_for_apartment = qty_of_nights * 65.00
    if 14 < qty_of_nights:
        price_for_apartment *= 0.90
elif month == 'June' or month == 'September':
    price_for_studio = qty_of_nights * 75.20
    if 14 < qty_of_nights:
        price_for_studio *= 0.80
    price_for_apartment = qty_of_nights * 68.70
    if 14 < qty_of_nights:
        price_for_apartment *= 0.90
elif month == 'July' or month == 'August':
    price_for_studio = qty_of_nights * 76.00
    price_for_apartment = qty_of_nights * 77.00
    if 14 < qty_of_nights:
        price_for_apartment *= 0.90

print(f'Apartment: {price_for_apartment:.2f} lv.')
print(f"Studio: {price_for_studio:.2f} lv.")