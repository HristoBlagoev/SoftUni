holiday_price = float(input())
volume_of_puzzles = int(input())
volume_of_dolls = int(input())
volume_of_bears = int(input())
volume_of_minions = int(input())
volume_of_trucks = int(input())
difference = 0

total_price = volume_of_puzzles * 2.6 + \
              volume_of_dolls * 3 + \
              volume_of_bears * 4.10 + \
              volume_of_minions * 8.20 + \
              volume_of_trucks * 2

total_volume = volume_of_puzzles \
               + volume_of_dolls \
               + volume_of_bears \
               + volume_of_minions \
               + volume_of_trucks

if total_volume >= 50:
    total_price *= 0.75
total_price *= 0.90

difference = abs(total_price - holiday_price)

if total_price >= holiday_price:
    print(f'Yes! {difference:.2f} lv left.')
else:
    print(f'Not enough money! {difference:.2f} lv needed.')
