number = int(input())
num_str = str(number)

for first_digit in range(1, int(num_str[2]) + 1):
    for second_digit in range(1, int(num_str[1]) + 1):
        for third_digit in range(1, int(num_str[0]) + 1):
            result = first_digit * second_digit * third_digit
            print(f'{first_digit} * {second_digit} * {third_digit} = {result};')


-------------------------------------------------
number = int(input())

first_digit = number % 10
second_digit = number // 10 % 10
third_digit = number // 100 % 10

for num1 in range(1, first_digit + 1):
    for num2 in range(1, second_digit + 1):
        for num3 in range(1, third_digit + 1):
            result = num1 * num2 * num3
            print(f"{num1} * {num2} * {num3} = {result};")