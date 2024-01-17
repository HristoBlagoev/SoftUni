fruit = input()
day_of_week = input()
qty = float(input())
price = 0
is_input_valid = True

if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' \
        or day_of_week == 'Thursday' or day_of_week == 'Friday':
        if fruit == 'banana':
            price = 2.50 * qty
        elif fruit == 'apple':
            price = 1.20 * qty
        elif fruit == 'orange':
            price = 0.85 * qty
        elif fruit == 'grapefruit':
            price = 1.45 * qty
        elif fruit == 'kiwi':
            price = 2.70 * qty
        elif fruit == 'pineapple':
            price = 5.50 * qty
        elif fruit == 'grapes':
            price = 3.85 * qty
        else:
            is_input_valid = False
elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
    if fruit == 'banana':
        price = 2.70 * qty
    elif fruit == 'apple':
        price = 1.25 * qty
    elif fruit == 'orange':
        price = 0.90 * qty
    elif fruit == 'grapefruit':
        price = 1.60 * qty
    elif fruit == 'kiwi':
        price = 3.00 * qty
    elif fruit == 'pineapple':
        price = 5.60 * qty
    elif fruit == 'grapes':
        price = 4.20 * qty
    else:
        is_input_valid = False
else:
    is_input_valid = False

if not is_input_valid:
    print('error')
else:
    print(f'{price:.2f}')