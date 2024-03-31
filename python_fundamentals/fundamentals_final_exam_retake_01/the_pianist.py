collection = {}


def add_piece(piece, composer, key):
    if piece in collection:
        print(f"{piece} is already in the collection!")
    else:
        collection[piece] = (composer, key)
        print(f"{piece} by {composer} in {key} added to the collection!")


def remove_piece(piece):
    if piece in collection:
        del collection[piece]
        print(f"Successfully removed {piece}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")


def change_key(piece, new_key):
    if piece in collection:
        composer, old_key = collection[piece]
        collection[piece] = (composer, new_key)
        print(f"Changed the key of {piece} to {new_key}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")


number_of_pieces = int(input())

for i in range(number_of_pieces):
    piece, composer, key = input().split("|")
    collection[piece] = (composer, key)

while True:
    command = input()

    if command == "Stop":
        break
    tokens = command.split("|")
    action = tokens[0]
    if action == "Add":
        add_piece(tokens[1], tokens[2], tokens[3])
    elif action == "Remove":
        remove_piece(tokens[1])
    elif action == "ChangeKey":
        change_key(tokens[1],tokens[2])

for piece, (composer, key) in (collection.items()):
    print(f"{piece} -> Composer: {composer}, Key: {key}")




