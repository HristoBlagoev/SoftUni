number_of_digits = int(input())

positive_numbers = []
negative_numbers = []

for numbers in range(number_of_digits):
    current_number = int(input())
    if current_number >= 0:
        positive_numbers.append(current_number)
    elif current_number < 0:
        negative_numbers.append(current_number)

print(positive_numbers)
print(negative_numbers)
print(f"Count of positives: {len(positive_numbers)} \n Sum of negatives: {sum(negative_numbers)}")