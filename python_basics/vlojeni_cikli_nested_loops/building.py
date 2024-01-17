qty_of_floors = int(input())
qty_of_rooms = int(input())


for floor in reversed(range(1, qty_of_floors + 1)):
    room_type = 'A' if floor % 2 else 'O'

    if floor == qty_of_floors:
        room_type = 'L'

    for room in range(qty_of_rooms):
        room_name = f'{room_type }{floor}{room}'
        print(room_name, end=" ")

    print()