foods_and_quantity = input().split()
final_products = {}

for index in range(0, len(foods_and_quantity), 2):
    product = foods_and_quantity[index]
    quantity = int(foods_and_quantity[index + 1])
    final_products[product] = quantity
print(final_products)
