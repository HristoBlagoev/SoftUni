def print_cupid_main_logic(neighborhood):
    print(f"Cupid's last position was {last_position_index}.")

    if sum(neighborhood) == 0:
        print("Mission was successful.")
    else:
        failed_houses = [house for house in neighborhood if house != 0]
        print(f"Cupid has failed {failed_houses} places.")


def cupid_main_logic(neighborhood):
    current_index = 0

    while True:
        command = input()

        if command == 'Love!':
            break

        command_split = command.split()
        step =







data = list(map(int, input().split('@')))
neighborhood =
