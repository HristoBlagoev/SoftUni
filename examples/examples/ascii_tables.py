name = 'Mario'

ascii_score_per_name = 0

for letter in name:
    ascii_score_per_name += ord(letter)

print(ascii_score_per_name)