first_player_name = input()
second_player_name = input()

difference = 0
is_number_wars = False

command = input()
while command != 'End of game':
    first_player_points_counter = 0
    second_player_points_counter = 0
    first_player_card = int(command)
    second_player_card = int(command)
    if first_player_card > second_player_card:
        result = abs(first_player_card - second_player_card)
        first_player_points_counter += result
    elif first_player_card < second_player_card:
        result = abs(first_player_card - second_player_card)
        second_player_points_counter += result

print(result)
command = input()