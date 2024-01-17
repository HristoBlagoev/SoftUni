start_char = 32
end_char = 126

print("ASCII TABLE")
print('-----------')

for i in range(8):
    for j in range(16):
        ascii_code = start_char + i + j * 8

        if ascii_code <= end_char:
            print(f'{ascii_code:3}:{chr(ascii_code)}', end=' | ')
        else:
            print(' ' * 10, end=' | ')
    print()
