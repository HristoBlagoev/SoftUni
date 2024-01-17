day = int(input())
output = ''

if day == 1:
    output = 'Monday'
elif day == 2:
    output = 'Tuesday'
elif day == 3:
    output = 'Wednesday'
elif day == 4:
    output = 'Thursday'
elif day == 5:
    output = 'Friday'
elif day == 6:
    output = 'Saturday'
elif day == 7:
    output = 'Sunday'
else:
    output = 'Error'

print(output)