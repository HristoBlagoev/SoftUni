numbers_in_strings = input().split(', ')
numbers_in_integers = [int(number) for number in numbers_in_strings]
for number in numbers_in_integers:
    if number == 0:
        numbers_in_integers.remove(number)
        numbers_in_integers.append(number)


print(numbers_in_integers)
