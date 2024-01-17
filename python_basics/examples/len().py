text = input()
length = len(text)

if length == 5:
    print('Yes')
else:
    print('No')

----------------
....
for judges in range(qty_judges):
    name_evaluator = input()
    points = float(input())

    total_points += len(name_evaluator) * points / 2
....