foods_and_quantity = input().split()
searched_products = input().split()

final_products = {}

for index in range(0, len(foods_and_quantity), 2):
    product = foods_and_quantity[index]
    quantity = int(foods_and_quantity[index + 1])
    final_products[product] = quantity
for product in searched_products:
    if product in final_products.keys():
        print(f"We have {final_products[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")