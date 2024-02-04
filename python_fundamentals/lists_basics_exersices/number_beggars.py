money_as_a_string = input().split(", ")
number_of_beggars = int(input())

money_as_integer = []

for money in money_as_a_string:
    money_as_integer.append(int(money))

final_sums = []
start_index = 0

for current_beggar in range(number_of_beggars):
    current_beggar_sum = 0
    for current_index in range(start_index, len(money_as_integer), number_of_beggars):
        current_beggar_sum += money_as_integer[current_index]
    final_sums.append(current_beggar_sum)
    start_index += 1
print(final_sums)
