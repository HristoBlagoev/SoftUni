number_of_lines = int(input())

numbers = []

for i in range(number_of_lines):
    number = int(input())
    numbers.append(number)

command = input()

filtrated_numbers = []

if command == 'even':
    for num in numbers:
        if num % 2 == 0:
            filtrated_numbers.append(num)

elif command == 'odd':
    for num in numbers:
        if num % 2 != 0:
            filtrated_numbers.append(num)

elif command == 'negative':
    for num in numbers:
        if num < 0:
            filtrated_numbers.append(num)

elif command == 'positive':
    for num in numbers:
        if num >= 0:
            filtrated_numbers.append(num)

print(filtrated_numbers)