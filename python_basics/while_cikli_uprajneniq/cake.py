width = int(input())
length = int(input())
total_pieces = width * length
cake_is_over = False
command = input()
while command != "STOP":
    current_pieces = int(command)
    total_pieces -= current_pieces
    if total_pieces < 0:
        cake_is_over = True
        break
    command = input()
if cake_is_over: # if cake_is_over == True
    print(f"No more cake left! You need {abs(total_pieces)} pieces more.")
else:
    print(f"{total_pieces} pieces are left.")