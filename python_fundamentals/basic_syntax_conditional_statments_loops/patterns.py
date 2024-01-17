number = int(input())

for r in range(1, number + 2):
    for k in range(1, r):
        print('*', end='')
    print()

for r in range(number - 1, 0, -1):
    for k in range(0, r):
        print('*', end='')
    print()