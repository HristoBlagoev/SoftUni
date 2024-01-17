number_packs_of_pens = int(input())
number_packs_of_markers = int(input())
liters_of_liquid = int(input())
discount_percent = int(input())
price_pens = 5.80
price_markers = 7.20
price_liquid = 1.20
needed_sum = number_packs_of_markers * price_markers \
             + number_packs_of_pens * price_pens \
             + liters_of_liquid * price_liquid
needed_sum_with_discount = needed_sum - needed_sum * discount_percent / 100

print(needed_sum_with_discount)

