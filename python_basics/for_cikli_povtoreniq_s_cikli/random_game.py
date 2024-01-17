import random

print('Welcome to the SoftUni Number Guessing Game!')
print('I have selected a random number between 1 and 100. Try to guess it')

secret_number = random.randint(1, 100)

for attempt in range (1, 6):
    guess = int(input('Enter your number: '))

    if guess == secret_number:
        print(f"Congratulations! you guess the correct number in {attempt} attempts")
        break

    elif guess < secret_number:
        print('Too low. Try again!')
    else:
        print("Too high. Try again!")

else:
    print(f'Sorry! you\'ve run out of attempts. The correct number was {secret_number}')
