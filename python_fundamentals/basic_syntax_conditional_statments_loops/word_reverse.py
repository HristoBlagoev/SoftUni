word = input()

reversed_word = ''

for current_symbol in range(len(word) - 1, - 1, - 1):
    reversed_word += word[current_symbol]
print(reversed_word)
