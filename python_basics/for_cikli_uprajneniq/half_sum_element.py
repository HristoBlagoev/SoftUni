from math import inf

count_of_numbers = int(input())
total_sum = 0
max_number = -inf

for i in range(count_of_numbers):
    number = int(input())
    total_sum += number
    if number > max_number:
        max_number = number

if max_number == total_sum - max_number:
    print('Yes')
    print(f'Sum = {max_number}')

else:
    difference = abs(max_number - (total_sum - max_number))
    print('No')
    print(f'Diff = {difference}')