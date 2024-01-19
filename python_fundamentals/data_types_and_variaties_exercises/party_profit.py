number_of_companion = int(input())
days = int(input())
coins = 0

for current_day in range(1, days + 1):
    if current_day % 10 == 0:
        number_of_companion -= 2
    if current_day % 15 == 0:
        number_of_companion += 5
    if current_day % 3 == 0:
        coins -= number_of_companion * 3
    if current_day % 5 == 0:
        coins += number_of_companion * 20
        if current_day % 3 == 0:
            coins -= number_of_companion * 2
    coins += 50
    coins -= number_of_companion * 2
coins_per_companion = coins // number_of_companion
print(f"{number_of_companion} companions received {coins_per_companion} coins each.")
