from math import ceil, floor

length_in_m = float(input())
width_in_m = float(input())

length_of_hall_in_sm = length_in_m * 100
width_of_hall_in_sm = width_in_m * 100
width_of_hall_without_the_corridor = width_of_hall_in_sm - 100

qty_of_desk_for_width = floor(width_of_hall_without_the_corridor / 70)
qty_of_desk_for_length = floor(length_of_hall_in_sm / 120)
qty_of_desks = qty_of_desk_for_length * qty_of_desk_for_width - 3


print(qty_of_desks)
