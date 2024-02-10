line_a = input()
line_b = input()
line_c = input()

output = 'Draw!'

list_a = [int(x) for x in line_a.split(' ') ]
list_b = [int(x) for x in line_b.split(' ') ]
list_c = [int(x) for x in line_c.split(' ') ]

matrix = [list_a, list_b, list_c]

for row in range(3):
    if matrix[row][0] == matrix[row][1] == matrix[row][2] == 1:
        output = 'First player won'
    elif matrix[row][0] == matrix[row][1] == matrix[row][2] == 2:
        output = 'Second player won'

for column in range(3):
    if matrix[0][column] == matrix[1][column] == matrix[2][column] == 1:
        output = 'First player won'
    elif matrix[0][column] == matrix[1][column] == matrix[2][column] == 2:
        output = 'Second player won'

if matrix[0][0] == matrix[1][1] == matrix[2][2] == 1:
    output = 'First player won'

if matrix[0][0] == matrix[1][1] == matrix[2][2] == 2:
    output = 'Second player won'

if matrix[2][0] == matrix[1][1] == matrix[0][2] == 1:
    output = 'First player won'

if matrix[2][0] == matrix[1][1] == matrix[0][2] == 2:
    output = 'Second player won'

print(output)
