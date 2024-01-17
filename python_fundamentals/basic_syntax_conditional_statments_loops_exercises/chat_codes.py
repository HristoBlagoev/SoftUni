number_of_messages = int(input())

for current_messages in range(number_of_messages):
    number = int(input())
    message = ""
    if number == 88:
        messages = "Hello"
    elif number == 86:
        messages = "How are you?"
    elif number < 88:
        messages = "GREAT!"
    elif number > 88:
        messages = "Bye."
    print(messages)
