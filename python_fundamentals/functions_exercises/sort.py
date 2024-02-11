my_list_with_string = input().split()
my_list_with_integers = [int(number) for number in my_list_with_string]

print(sorted(my_list_with_integers))