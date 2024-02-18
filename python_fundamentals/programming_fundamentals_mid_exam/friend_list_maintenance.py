user_names = input().split(', ')

blacklisted_count = 0
lost_count = 0

command = input().split()

while command[0] != 'Report':
    action = command[0]

    if action == 'Blacklist':
        name = command[1]
        if name in user_names:
            user_names[user_names.index(name)] = 'Blacklisted'
            print(f"{name} was blacklisted.")
            blacklisted_count += 1
        else:
            print(f"{name} was not found.")
    elif action == 'Error':
        index = int(command[1])
        if 0 <= index < len(user_names) and user_names[index] != 'Blacklisted' and user_names[index] != "Lost":
            print(f"{user_names[index]} was lost due to an error.")
            user_names[index] = 'Lost'
            lost_count += 1
    elif action == 'Change':
        index = int(command[1])
        new_name = command[2]
        if 0 <= index < len(user_names):
            current_name = user_names[index]
            user_names[index] = new_name
            print(f"{current_name} changed his username to {new_name}.")

    command = input().split()

print(f"Blacklisted names: {blacklisted_count}")
print(f"Lost names: {lost_count}")
print(" ".join(user_names))
