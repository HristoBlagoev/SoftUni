number_of_stings = int(input())
word = input()

list_of_strings = []


for course in range(number_of_stings):
    current_course = input()
    list_of_strings.append(current_course)
print(list_of_strings)

for i in range(len(list_of_strings) - 1, -1, -1):
    element = list_of_strings[i]
    if word not in element:
        list_of_strings.remove(element)
print(list_of_strings)

