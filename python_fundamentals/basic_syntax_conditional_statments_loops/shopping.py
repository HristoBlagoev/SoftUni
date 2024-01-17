budget = int(input())
spend_money = 0

command = input()

while command != "End":
    price_of_product = int(command)
    spend_money += price_of_product
    if spend_money > budget:
        print('You went in overdraft!')
        break
    command = input()
else:
    print('You bought everything needed.')


