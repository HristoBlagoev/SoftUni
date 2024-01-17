flag = False

while True:
    username = input()

    if username == 'End':
        flag = True
        break

if flag:
    print('Break Condition!')