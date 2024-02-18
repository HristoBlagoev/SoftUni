friends = input().split(", ")
blacklisted_count = 0
lost_count = 0

while True:
    command = input().split()
    if command[0] == "Report":
        break
    elif command[0] == "Blacklist":
        name = command[1]
        if name in friends:
            friends[friends.index(name)] = "Blacklisted"
            print(f"{name} was blacklisted.")
            blacklisted_count += 1
        else:
            print(f"{name} was not found.")
    elif command[0] == "Error":
        index = int(command[1])
        if 0 <= index < len(friends) and friends[index] != "Blacklisted" and friends[index] != "Lost":
            print(f"{friends[index]} was lost due to an error.")
            friends[index] = "Lost"
            lost_count += 1
    elif command[0] == "Change":
        index = int(command[1])
        new_name = command[2]
        if 0 <= index < len(friends):
            current_name = friends[index]
            friends[index] = new_name
            print(f"{current_name} changed his username to {new_name}.")

print(f"Blacklisted names: {blacklisted_count}")
print(f"Lost names: {lost_count}")
print(" ".join(friends))