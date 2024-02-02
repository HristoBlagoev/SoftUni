

number_list = input().split()

absolute_value = []

for number in number_list:
    absolute_value.append(abs(float(number)))

print(absolute_value)