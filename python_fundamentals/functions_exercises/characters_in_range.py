def chars_range(first_char, second_char):
    result = ''

    for index in range(ord(first_char) + 1, ord(second_char)):
        result += chr(index) + " "

    return result


char1= input()
char2= input()
print(chars_range(char1, char2))

---------------------------------------------------

chars_range = lambda first_char, second_char: ' '.join(map(chr, range(ord(first_char) + 1, ord(second_char))))
char1 = input()
char2 = input()

print(chars_range(char1, char2))

