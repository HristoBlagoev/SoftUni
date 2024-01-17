from sys import maxsize

min_number = maxsize

while True:
    text = input()

    if text == 'Stop':
        break

    current_number = int(text)

    if current_number < min_number:
        min_number = current_number

print(min_number)