quantity_of_chicken_meal = int(input())
quantity_of_fish_menu = int(input())
quantity_of_vegetarian_meal = int(input())

price_chicken = 10.35
price_fish = 12.40
price_vegetarian = 8.15
price_delivery = 2.50

average_price_for_meals = price_chicken * quantity_of_chicken_meal +\
                          price_fish * quantity_of_fish_menu + \
                          price_vegetarian * quantity_of_vegetarian_meal
price_desert = average_price_for_meals * 0.2
total_price = average_price_for_meals + price_delivery + price_desert

print(total_price)
