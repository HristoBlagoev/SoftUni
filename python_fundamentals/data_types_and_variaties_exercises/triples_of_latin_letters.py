number_of_characters = int(input())

for first_symbol in range(number_of_characters):
    for second_symbol in range(number_of_characters):
        for third_symbol in range(number_of_characters):
            print(f'{chr(97+first_symbol)}{chr(97+second_symbol)}{chr(97+third_symbol)}')