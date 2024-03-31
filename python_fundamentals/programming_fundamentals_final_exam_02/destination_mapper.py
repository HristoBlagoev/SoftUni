import re


def valid_destination_function(dest_data):
    pattern = r"([=|\/])([A-Z][A-Za-z]{3,})\1"
    matches = []
    travel_points = 0
    result = re.finditer(pattern, dest_data)

    for current_destination in result:
        matches.append(current_destination.group(2))
        travel_points += len(current_destination.group(2))

    print(f"Destinations: {', '.join(matches)} \nTravel Points: {travel_points}")


data = input()

valid_destination_function(data)
