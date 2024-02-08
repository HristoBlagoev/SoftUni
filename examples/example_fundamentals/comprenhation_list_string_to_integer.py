my_list_with_string = ['1', '2', '3']
my_list_with_integers = [int(number) for number in my_list_with_string]

print(my_list_with_string)
print(my_list_with_integers)
-------------------------------
list_with_numbers = input().split()
opposite_numbers = []

for number in list_with_numbers:
    opposite_number = -int(number)
    opposite_numbers.append(opposite_number)
print(opposite_numbers)

print([-int(number) for number in input().split()])
--------------------------------
print(["A-" + str(number) for number in range(1, 12)])
--------------------------------
numbers = [1, 2, 3, 4, 5, 6]

result = [num ** 2 if num % 2 == 0 else num ** 3 for num in numbers]

print(result)