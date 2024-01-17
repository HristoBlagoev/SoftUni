from math import ceil

number_of_people = int(input())
price_entrance_per_person = float(input())
price_deck_chair_per_person = float(input())
price_umbrella_per_person = float(input())


number_of_deck_chairs = ceil(number_of_people * 0.75)
number_of_umbrellas = ceil(number_of_people * 0.50)
total_price_entrance = number_of_people * price_entrance_per_person
total_price_deck_chairs = number_of_deck_chairs * price_deck_chair_per_person
total_price_umbrellas = number_of_umbrellas * price_umbrella_per_person
total_price = total_price_entrance + total_price_deck_chairs + total_price_umbrellas

print(f"{total_price:.2f} lv." )
