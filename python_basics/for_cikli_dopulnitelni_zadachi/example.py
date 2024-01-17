inherited_money = float(input())
target_year = int(input())

current_age = 18
starting_year = 1800
yearly_expenses = 12000

for current_year in range(starting_year, target_year + 1):
    if current_year % 2 == 0:
        inherited_money -= yearly_expenses
    else:
        inherited_money -= yearly_expenses + current_age * 50
    current_age += 1

if inherited_money < 0:
    print(f'He will need {abs(inherited_money):.2f} dollars to survive.')
else:
    print(f'Yes! He will live a carefree life and will have {inherited_money:.2f} dollars left.')