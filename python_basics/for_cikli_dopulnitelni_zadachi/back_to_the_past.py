inherited_money = float(input())
year_to_live = int(input())

current_ages = 18
yearly_expenses = 12000
starting_year = 1800

for current_year in range(starting_year, year_to_live + 1):
    if current_year % 2 == 0:
        inherited_money -= yearly_expenses
    else:
        inherited_money -= yearly_expenses + current_ages * 50
        current_ages += 1

if inherited_money < 0:
    print(f'He will need {abs(inherited_money):.2f} dollars to survive.')
else:
    print(f'Yes! He will live a carefree life and will have {inherited_money:.2f} dollars left.')


