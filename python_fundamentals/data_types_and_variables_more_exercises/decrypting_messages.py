key = int(input())
number_of_letters = int(input())

for letter in range(number_of_letters):
    current_letter = input()
    message = (ord(current_letter) + key)
    print(chr(message), end="")
