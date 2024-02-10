first_sequence = input().split(", ")
second_sequence = input().split(", ")

substrings_list = []

for first_string in first_sequence:
    for second_sting in second_sequence:
        if first_string in second_sting:
            substrings_list.append(first_string)
            break
print(substrings_list)
