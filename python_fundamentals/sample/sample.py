strings = int(input())

for i in range(strings):
    current_string = str(input())

    if "_" in current_string or "," in current_string or "." in current_string:
        print(f"{current_string} is not pure!")
    else:
        print(f"{current_string} is pure.")

