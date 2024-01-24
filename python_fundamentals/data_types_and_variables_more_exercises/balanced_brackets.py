num_of_lines = int(input())
times_open = 0
times_closed = 0

for i in range(num_of_lines):
    str = input()
    if str == "(":
        times_open += 1
        if times_open == 2:
            print("UNBALANCED")
            break
    if times_open == 0 and str == ")":
        print("UNBALANCED")
        break
    if times_open == 1 and str == ")":
        times_closed += 1
        if times_closed == 2:
            print("UNBALANCED")
            break
    if times_open == 1 and times_closed == 1:
        print("BALANCED")
        break