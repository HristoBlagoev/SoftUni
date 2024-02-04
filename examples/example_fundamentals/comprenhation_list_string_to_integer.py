my_list_with_string = ['1', '2', '3']
my_list_with_integers = [int(number) for number in my_list_with_string]

print(my_list_with_string)
print(my_list_with_integers)




list_with_numbers = input().split()
opposite_numbers = []

for number in list_with_numbers:
    opposite_number = -int(number)
    opposite_numbers.append(opposite_number)

print(opposite_numbers)


print([-int(number) for number in input().split()])