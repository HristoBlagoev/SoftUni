price_without_taxes = 0
price_with_taxes = 0

while True:
    command = input()

    if command == 'special' or command == 'regular':
        break
    current_price = float(command)
    if current_price < 0:
        print("Invalid price!")
        continue
    price_without_taxes += current_price
    price_with_taxes = price_without_taxes * 1.20
    taxes = abs(price_with_taxes - price_without_taxes)
if command == 'special':
    price_with_taxes *= 0.90

if price_with_taxes > 0:
    print(f"Congratulations you've just bought a new computer!\n"
        f"Price without taxes: {price_without_taxes:.2f}$\n"
        f"Taxes: {taxes:.2f}$\n-----------\n"
        f"Total price: {price_with_taxes:.2f}$")
else:
    print('Invalid order!')

