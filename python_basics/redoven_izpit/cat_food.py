qty_of_cats = int(input())

group_1 = 0
group_2 = 0
group_3 = 0
food_counter = 0

for cats in range(qty_of_cats):
    current_cat_food_volume = float(input())
    if 100 <= current_cat_food_volume < 200:
        group_1 += 1
        food_counter += current_cat_food_volume
    elif 200 <= current_cat_food_volume < 300:
        group_2 += 1
        food_counter += current_cat_food_volume
    elif 300 <= current_cat_food_volume < 400:
        group_3 += 1
        food_counter += current_cat_food_volume

food_counter_in_kg = food_counter / 1000
price_for_food = food_counter_in_kg * 12.45

print(f"Group 1: {group_1} cats.")
print(f"Group 2: {group_2} cats.")
print(f"Group 3: {group_3} cats.")
print(f"Price for food per day: {price_for_food:.2f} lv.")