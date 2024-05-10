import sys
import msvcrt
import os
clear = lambda: os.system('cls')

grid = []
col = []
row = []

i = 0
for n in range(20):
    row.append(i)
    i += 1

i = 0
for n in range(20):
    col.append(i)
    i += 1

grid.append(col)
grid.append(row)

def get_direction():
    location_change = [0 ,0]
    dir = msvcrt.getch()
    if dir == b"w":
        location_change[1] = -1
    elif dir == b"s":
        location_change[1] = 1
    elif dir == b"a":
        location_change[0] = -1
    elif dir == b"d":
        location_change[0] = 1
    elif dir == b"q":
        sys.exit()

    return location_change

def display_map():
    clear()
    blank = "███"
    line = ""
    player = " X "
    empty_line = blank * len(grid[0])
    for n in grid[0]:
        if n == current_location[0]:
            line += player
        else:
            line += blank

    top_bar = "   "
    i = 0
    for n in range(len(grid[0])):
        if i < 10:
            top_bar += f" {i} "
        else:
            top_bar += f"{i} "
        i += 1

    print(top_bar)

    i = 0
    for n in grid[1]:
        if n == current_location[1]:
            if i < 10:
                print(f" {i} {line}")
            else:
                print(f"{i} {line}")
        else:
            if i < 10:
                print(f" {i} {empty_line}")
            else:
                print(f"{i} {empty_line}")
        i += 1

indexes = [0, 0]
current_location = grid[0][indexes[0]], grid[1][indexes[1]]
print(current_location)
display_map()

zmiana = []
while True:
    if indexes[0] < 10:
            col = " "
    else:
        col = ""
    if indexes[1] < 10:
            row = " "
    else:
        row = ""   

    print(f"   Pozycja: x:{grid[0][current_location[0]]}{col} y:{grid[1][current_location[1]]}{row} Sterowanie - ruch: [WSAD], wyjście: [Q]")
    zmiana = get_direction()

    if indexes[0] <= 0:
        if zmiana[0] > 0:
            indexes[0] += zmiana[0]
    elif indexes[0] < len(grid[0]) - 1:
        indexes[0] += zmiana[0]
    elif indexes[0] >= len(grid[0]) - 1:
        if zmiana[0] < 0:
            indexes[0] += zmiana[0]

    if indexes[1] <= 0:
        if zmiana[1] > 0:
            indexes[1] += zmiana[1]
    elif indexes[1] < len(grid[0]) - 1:
        indexes[1] += zmiana[1]
    elif indexes[1] >= len(grid[0]) - 1:
        if zmiana[1] < 0:
            indexes[1] += zmiana[1]

    current_location = grid[0][indexes[0]], grid[1][indexes[1]]
    display_map()





