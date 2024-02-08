numbers_str = input().split()

numbers = []

for num in numbers_str:
    numbers.append(int(num))

remover = int(input())

for _ in range(remover):
    numbers.remove(min(numbers))

for index in range(0, len(numbers) - 1):
    print(f"{numbers[index]}, ", end="")
print(numbers[-1])

# numbers = list(map(int, input().split()))
# remover = [numbers.remove(min(numbers)) for _ in range(int(input()))]
#
# print(numbers)