message = input()
command = input()

while command != "Decode":
    command = command.split("|")
    action = command[0]

    if action == "Move":
        number_of_letters = int(command[1])
        message = message[number_of_letters:] + message[:number_of_letters]
    elif action == "Insert":
        index = int(command[1])
        value = command[2]
        message = message[:index] + value + message[index:]
    elif action == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        message = message.replace(substring, replacement)

    command = input()
print(f"The decrypted message is: {message}")
