budget = float(input())
flor_per_kilo_price = float(input())
eggs_per_pack_price = flor_per_kilo_price * 0.75
milk_per_liter_price = flor_per_kilo_price * 1.25

loaf_price = flor_per_kilo_price + eggs_per_pack_price + (milk_per_liter_price * 0.25)

colored_eggs_counter = 0
bread_counter = 0

while budget > 0:
    if budget < loaf_price:
        break
    bread_counter += 1
    budget -= loaf_price
    colored_eggs_counter += 3
    if bread_counter % 3 == 0:
        colored_eggs_counter -= bread_counter -2

print(f"You made {bread_counter} loaves of Easter bread! Now you have {colored_eggs_counter} eggs and {budget:.2f}BGN left.")