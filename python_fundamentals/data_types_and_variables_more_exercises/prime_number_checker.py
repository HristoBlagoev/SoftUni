import math

n = int(input())
prime = True

if n > 1:
    for i in range(2, math.floor(math.sqrt(n) + 1)):
        if n % i == 0:
            prime = False
            break
else:
    prime = False

if prime:
    print('True')
else:
    print('False')



import math

number = int(input())

prime = True

if number > 1:
    for digit in range(2, math.floor(math.sqrt(number) + 1)):
        if number % digit == 0:
            prime = False
            break
    if prime:
        print("True")
    else:
        print("False")