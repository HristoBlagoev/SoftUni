def find_smallest(a, b, c):
    return min(a, b, c)


first_number = int(input())
second_number = int(input())
third_number = int(input())

result = find_smallest(first_number, second_number, third_number)

print(result)