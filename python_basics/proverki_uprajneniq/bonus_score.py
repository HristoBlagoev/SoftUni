points = int(input())
bonus_points = 0

if 100 >= points:
    bonus_points = 5
elif points > 1000:
    bonus_points = points * 0.10
else:
    bonus_points = points * 0.20

if points % 2 == 0:
    bonus_points += 1 # bonus_points = bonus_points +1
elif points % 10 == 5:
    bonus_points += 2 # bonus_points = bonus_points +2

total_points = points + bonus_points

print(bonus_points)
print(total_points)
