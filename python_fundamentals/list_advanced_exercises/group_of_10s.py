numbers = [int(number) for number in input().split(', ')]
current_group = 10
while numbers:
    filtrated_numbers_for_current_group = [number for number in numbers if number <= current_group]
    print(f"Group of {current_group}'s: {filtrated_numbers_for_current_group}")
    current_group += 10
    numbers = [number for number in numbers if number not in filtrated_numbers_for_current_group]