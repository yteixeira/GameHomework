import random
max = 6
rows, cols = (max, max)
gameOver = False

posX = random.randint(0, max -1)
posY = random.randint(0, max -1)
value = ""

goal = 5
gPosX = random.randint(0, max -1)
gPosY = random.randint(0, max -1)

enemy = 1
ePosX = random.randint(0, max -1)
ePosY = random.randint(0, max -1)

while gameOver == False:
    grid = [[0 for i in range(cols)] for j in range(rows)]
    grid[gPosY][gPosX] = goal
    grid[posY][posX] = 8
    grid[ePosY][ePosX] = enemy

    for row in grid:
        print(row)

    #win and lose states
    if grid[posY][posX] == grid[gPosY][gPosX]:
        print("YOU WON !!")
        gameOver = True
    elif grid[posY][posX] == grid[ePosY][ePosX]:
        print("You Lost :(")
        gameOver = True
    else:
        value = input("What is your move? ")

    if value == "up" and posY > 0:
        posY -= 1
    elif value == "down" and posY < max -1:
        posY += 1
    elif value == "left" and posX > 0:
        posX -= 1
    elif value == "right" and posX < max -1:
        posX += 1
    elif value == "end":
        print("see you later alligator")
        gameOver = True
    else:
        print("invalid value")

    #Enemy Movement
    if ePosX > 0 and ePosX < max -1:
        ePosX += random.randint(-1, 1)
    elif ePosX == 0:
        ePosX += random.randint(0, 1)
    elif ePosX == max -1:
        ePosX += random.randint(-1, 0)

    if ePosY > 0 and ePosY < max -1:
        ePosY += random.randint(-1, 1)
    elif ePosY == 0:
        ePosY += random.randint(0, 1)
    elif ePosY == max -1:
        ePosY += random.randint(-1, 0)
