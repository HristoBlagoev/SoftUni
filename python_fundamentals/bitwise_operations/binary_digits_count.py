number = int(input())
binary_digit = B = int(input())

binary_digit_counter = 0

while number > 0:
    current_number = number % 2
    if current_number == binary_digit:
        binary_digit_counter += 1
    number = number // 2

print(binary_digit_counter)