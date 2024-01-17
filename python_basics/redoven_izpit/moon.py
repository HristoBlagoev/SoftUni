from math import ceil

average_speed_per_km = float(input())
fuel_per_100_km = float(input())

total_distance = 384400 * 2
round_trip_time = ceil(total_distance / average_speed_per_km)
total_spend_time = round_trip_time + 3
needed_fuel = ceil((fuel_per_100_km * total_distance) / 100)

print(total_spend_time)
print(needed_fuel)