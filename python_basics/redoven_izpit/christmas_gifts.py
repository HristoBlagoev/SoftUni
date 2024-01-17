command = input()
qty_of_adults = 0
qty_of_kids = 0
money_for_toys = 0
money_for_sweaters = 0

while command != 'Christmas':
    ages = int(command)
    if ages <= 16:
        qty_of_kids += 1
        money_for_toys += 5
    if ages > 16:
        qty_of_adults += 1
        money_for_sweaters += 15

    command = input()

print(f"Number of adults: {qty_of_adults}" )
print(f"Number of kids: {qty_of_kids}")
print(f"Money for toys: {money_for_toys}")
print(f"Money for sweaters: {money_for_sweaters}")