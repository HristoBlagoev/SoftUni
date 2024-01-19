lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_price = 0
shield_breaks = 0

for current_fights in range(1, lost_fights + 1):
    if current_fights % 2 == 0:
        total_price += helmet_price
    if current_fights % 3 == 0:
        total_price += sword_price
    if current_fights % (2*3) == 0:
        shield_breaks += 1
        total_price += shield_price
        if shield_breaks % 2 == 0:
            total_price += armor_price
print(f"Gladiator expenses: {total_price:.2f} aureus")
