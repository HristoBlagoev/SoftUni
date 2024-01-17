begin_of_interval = int(input())
end_of_interval = int(input())
magic_number = int(input())

combination_counter = 0

is_magic_number = False
for first_number in range(begin_of_interval, end_of_interval + 1):
    for second_number in range(begin_of_interval, end_of_interval + 1):
        combination_counter += 1
        if first_number + second_number == magic_number:
            print(f'Combination N:{combination_counter} ({first_number} + {second_number} = {magic_number})')
            is_magic_number = True
            break


    if is_magic_number:
        break
else:
    print(f"{combination_counter} combinations - neither equals {magic_number}")