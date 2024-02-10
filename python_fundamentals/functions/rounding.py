number_list = list(map(float, input().split()))
rounded_list = []

for number in number_list:
    rounded_list.append(round(number))

print(rounded_list)