my_list_with_string = input().split()
my_list_with_integers = [int(number) for number in my_list_with_string]

my_filtrated_list = filter(lambda x: x % 2 == 0, my_list_with_integers)

print(list(my_filtrated_list))