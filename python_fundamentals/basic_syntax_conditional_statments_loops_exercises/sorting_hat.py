command = input()

while command != 'Welcome!':
    if command == 'Voldemort':
        print("You must not speak of that name!")
        break
    current_name = len(command)
    if current_name < 5:
        print(f"{command} goes to Gryffindor.")
    elif current_name == 5:
        print(f"{command} goes to Slytherin.")
    elif current_name == 6:
        print(f"{command} goes to Ravenclaw.")
    elif current_name > 6:
        print(f"{command} goes to Hufflepuff.")
    command = input()
if command == "Welcome!":
    print("Welcome to Hogwarts.")
