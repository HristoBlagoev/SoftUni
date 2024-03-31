message = input()
command = input()
results = []
while command != "Finish":
    command = command.split()
    action = command[0]

    if action == "Replace":
        current_char, new_char = command[1], command[2]
        message = message.replace(current_char, new_char)
        results.append(message)
    elif action == "Cut":
        start_index, end_index = int(command[1]), int(command[2])
        if 0 <= start_index <= end_index < len(message):
            message = message[:start_index] + message[end_index + 1:]
            results.append(message)
        else:
            results.append("Invalid indices!")
    elif action == "Make":
        case = command[1]
        if case == "Upper":
            message = message.upper()
        elif case == "Lower":
            message = message.lower()
        results.append(message)
    elif action == "Check":
        string_to_check = command[1]
        if string_to_check in message:
            results.append(f"Message contains {string_to_check}")
        else:
            results.append(f"Message doesn't contain {string_to_check}")
    elif action == "Sum":
        start_index, end_index = int(command[1]), int(command[2])
        if 0<= start_index <= end_index < len(message):
            substring = message[start_index:end_index + 1]
            substring_sum = sum(ord(char) for char in substring)
            results.append(str(substring_sum))
        else:
            results.append("Invalid indices!")

    command = input()

for result in results:
    print(result)