number = float(input())

if number == 0:
    definer = 'zero'
elif number > 0:
    if number < 1:
        definer = 'small positive'
    elif number > 1000000:
        definer = 'large positive'
    else:
        definer = 'positive'
elif number < 0:
    if abs(number) < 1:
        definer = 'small negative'
    elif abs(number) > 1000000:
        definer = 'large negative'
    else:
        definer = 'negative'

print(definer)