world = [["_" for i in range(3)] for j in range(3)]
for w in world:
    a = ""
    for m in w:
        a += m
    print(a)

end = False
move = 0
wonx = False
wono = False
draw = False

while not end:
    player = input().split()
    x = player[0]
    y = player[1]
    if world[int(x) - 1][int(y) - 1] != "X" and world[int(x) - 1][int(y) - 1] != "O":
        if move % 2 == 0:
            world[int(x) - 1][int(y) - 1] = "X"
        else:
            world[int(x) - 1][int(y) - 1] = "O"
        move += 1
    else:
        print("The position is taken")
        continue

    for l in range(len(world)):
        t = 0
        for r in range(len(world)):
            if world[int(l)][int(r)] == "X":
                t += 1
        if t == 3:
            print("Winer")
            wonx = True

    for l in range(len(world)):
        t = 0
        for r in range(len(world)):
            if world[int(r)][int(l)] == "X":
                t += 1
        if t == 3:
            print("Winer")
            wonx = True

    if world[0][0] == "X" and world[1][1] == "X" and world[2][2] == "X":
        wonx = True
    elif world[0][2] == "X" and world[1][1] == "X" and world[2][0] == "X":
        wonx = True

    for l in range(len(world)):
        t = 0
        for r in range(len(world)):
            if world[int(l)][int(r)] == "O":
                t += 1
        if t == 3:
            print("Winer")
            wono = True

    for l in range(len(world)):
        t = 0
        for r in range(len(world)):
            if world[int(r)][int(l)] == "O":
                t += 1
        if t == 3:
            print("Winer")
            wono = True

    if world[0][0] == "O" and world[1][1] == "O" and world[2][2] == "O":
        wonx = True
    elif world[0][2] == "O" and world[1][1] == "O" and world[2][0] == "O":
        wonx = True

    for n in world:
        if "_" in n:
            pass
        else:
            draw = True

    for w in world:
        a = ""
        for m in w:
            a += m
        print(a)
    if wonx == True or wono == True or draw == True:
        break
if wonx:
    print(f"Congratulations player1\n You won")
elif wono:
    print(f"Congratulations player2\n You won")
else:
    print("Draw")