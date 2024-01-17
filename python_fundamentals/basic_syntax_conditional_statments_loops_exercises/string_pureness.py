number_of_strings = int(input())

for string in range(number_of_strings):
    current_string = input()
    is_pure_string = True
    for character in current_string:
        if character in(',', '.', '_'):
            print(f"{current_string} is not pure!")
            is_pure_string = False
            break
    if is_pure_string:
        print(f"{current_string} is pure.")


special_characters = "_,."
number = int(input())
for numbers in range(number):

    text = input()
    if any(char in special_characters for char in text):
        print(f"{text} is not pure!")
    else:
        print(f"{text} is pure.")



strings = int(input())
for i in range(strings):
    current_string = str(input())
    if "_" in current_string or "," in current_string or "." in current_string:
        print(f"{current_string} is not pure!")
    else:
        print(f"{current_string} is pure.")