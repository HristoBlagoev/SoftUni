stage_of_championship = input()
type_of_ticket = input()
qty_of_tickets = int(input())
picture_with_trophy = input()
price = 0

if stage_of_championship == 'Quarter final':
    if type_of_ticket == 'Standard':
        price = 55.50 * qty_of_tickets
    elif type_of_ticket == 'Premium':
        price = 105.20 * qty_of_tickets
    elif type_of_ticket == 'VIP':
        price = 118.90 * qty_of_tickets
elif stage_of_championship == 'Semi final':
    if type_of_ticket == 'Standard':
        price = 75.88 * qty_of_tickets
    elif type_of_ticket == 'Premium':
        price = 125.22 * qty_of_tickets
    elif type_of_ticket == 'VIP':
        price = 300.40 * qty_of_tickets
elif stage_of_championship == 'Final':
    if type_of_ticket == 'Standard':
        price = 110.10 * qty_of_tickets
    elif type_of_ticket == 'Premium':
        price = 160.66 * qty_of_tickets
    elif type_of_ticket == 'VIP':
        price = 400.00 * qty_of_tickets

current_price = price

if price > 4000:
    current_price *= 0.75
elif price > 2500:
    current_price *= 0.90

if picture_with_trophy == "Y" and price < 4000:
    total_price = current_price + 40 * qty_of_tickets
elif picture_with_trophy == "N":
    total_price = current_price
else:
    total_price = current_price

print(f'{total_price:.2f}')