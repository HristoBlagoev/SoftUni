def sorted_list():
    name_list = input().split(", ")
    sorted_names = sorted(name_list, key=lambda name: (-len(name), name))

    return sorted_names


result = sorted_list()

print(result)

# name_list = input().split(', ')
#
# sorted_name = sorted(name_list, key=lambda name: (-len(name), name))
#
# print(sorted_name)