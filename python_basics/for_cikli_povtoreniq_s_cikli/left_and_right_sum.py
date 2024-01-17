number = int(input())
difference = 0
left_sum = 0
right_sum = 0

for i in range(1, number + 1):
    current_number = int(input())
    left_sum += current_number
for i in range(1, number + 1):
    current_number = int(input())
    right_sum += current_number

difference = abs(right_sum - left_sum)

if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    print(f'No, diff = {difference}')

'''
-------------------------------------------------------------
qty_inputs = int(input())

sum_left = 0
sum_right = 0

for i in range(qty_inputs * 2):
    user_input = int(input())

    if i < qty_inputs:
        sum_left += user_input
    else:
        sum_right += user_input

difference = abs(sum_left - sum_right)

if difference == 0:
    print(f'Yes, sum = {sum_left}')
else:
    print(f'No, diff = {difference}')
'''