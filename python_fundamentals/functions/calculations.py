def multiply(number_1, number_2):
    return number_1 * number_2


def divide(number_1, number_2):
    return number_1 // number_2


def add(number_1, number_2):
    return number_1 + number_2


def subtract(number_1, number_2):
    return number_1 - number_2


operator = input()
first_number = int(input())
second_number = int(input())

if operator == "multiply":
    result = multiply(first_number, second_number)
elif operator == 'divide':
    result = divide(first_number, second_number)
elif operator == "add":
    result = add(first_number, second_number)
elif operator == 'subtract':
    result = subtract(first_number, second_number)

print(result)