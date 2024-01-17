import random
user_name = "Ivan"

print(f' Welcome to the Slot Machine Game!\nHello {user_name}!')

symbols = ['A', 'B', 'C', 'D', 'E', 'F']

balance = int(input('Enter your balance: '))

bet = 0

while balance > 0:
    print(30 * '*')
    print('Current Balance:', balance)

    while True:
        bet = int(input('Enter your bet amount (0 to exit): '))

        if bet == 0:
            break

        if bet > balance:
            print('Insufficient balance. Please a lower bet!')
        else:
            break
    if bet == 0:
        break

    balance -= bet

    print('>>>Spinning the reels >>>')
    reel1 = random.choice(symbols)
    reel2 = random.choice(symbols)
    reel3 = random.choice(symbols)

    print(reel1, reel2, reel3)

    if reel1 == reel2 == reel3:
        winnings = bet * 10
        balance += winnings
        print('Congratulations! You won Jackpot', winnings, 'nomey')

    elif reel1 == reel2 or reel2 == reel3:
        winnings = bet * 2
        balance += winnings
        print('Congratulations! You won', winnings, 'nomey')

    else:
        print('Sorry! no match. Better luck next time!')

if balance == 0:
    print('Game Over! Final Balance: 0\nPlease insert money to play again!')


