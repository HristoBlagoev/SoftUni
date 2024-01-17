country = input()
instrument = input()

if 'Russia' == country:
    if instrument == 'ribbon':
        difficulty = 9.100
        execution = 9.400
    elif instrument == 'hoop':
        difficulty = 9.300
        execution = 9.800
    elif instrument == 'rope':
        difficulty = 9.600
        execution = 9.000
elif country == 'Bulgaria':
    if instrument == 'ribbon':
        difficulty = 9.600
        execution = 9.400
    elif instrument == 'hoop':
        difficulty = 9.550
        execution = 9.750
    elif instrument == 'rope':
        difficulty = 9.500
        execution = 9.400
elif country == 'Italy':
    if instrument == 'ribbon':
        difficulty = 9.200
        execution = 9.500
    elif instrument == 'hoop':
        difficulty = 9.450
        execution = 9.350
    elif instrument == 'rope':
        difficulty = 9.700
        execution = 9.150

point_instrument = difficulty + execution
not_enough_points = 20 - point_instrument

percentage_not_enough_points = not_enough_points / 20 * 100

print(f"The team of {country} get {point_instrument:.3f} on {instrument}.")
print(f'{percentage_not_enough_points:.2f}%')