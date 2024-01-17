available_account_sum = 0

while True:
    text = input()

    if text == 'NoMoreMoney':
        break

    current_sum = float(text)

    if current_sum >= 0:
        available_account_sum += current_sum
        print(f'Increase: {current_sum:.02f}')
    else:
        print("Invalid operation!")
        break

print(f'Total: {available_account_sum:.2f}')
