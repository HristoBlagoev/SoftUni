number_list = input().split()

absolute_value = []

for number in number_list:
    absolute_value.append(abs(float(number)))

print(absolute_value)



number_list = input().split()

absolute_value_list = [abs(float(number)) for number in number_list]

print(absolute_value_list)
