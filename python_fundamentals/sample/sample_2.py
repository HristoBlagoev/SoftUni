list_input = input().split(", ")
new_list = []
for i in list_input:
    if int(i) == 0:
        list_input.remove(i)
        list_input.append(i)
for i in list_input:
    new_list.append(int(i))

print(new_list)