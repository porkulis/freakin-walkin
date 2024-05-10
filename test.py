import sys
import os
clear = lambda: os.system('cls')

grid = []
col = []
row = []

i = 0
for n in range(15):
    row.append(i)
    i += 1

i = 0
for n in range(15):
    col.append(i)
    i += 1

#col = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

grid.append(col)
grid.append(row)

def get_direction():
    location_change = [0 ,0]
    dir = input("Sterowanie [WSAD] + ENTER. [Q] - wyjście.\nKierunek: ")
    if dir == "w":
        location_change[1] = -1
    elif dir == "s":
        location_change[1] = 1
    elif dir == "a":
        location_change[0] = -1
    elif dir == "d":
        location_change[0] = 1
    elif dir == "q":
        sys.exit()
    return location_change

def display_map():
    clear()
    blank = " - "
    line = ""
    empty_line = blank * len(grid[0])
    for n in grid[0]:
        if n == current_location[0]:
            line += " █ "
        else:
            line += blank
    #print("Sterowanie: wsad + Enter. \"Q\" by wyjść.\n")
    #print("    a  b  c  d  e  f  g  h  i  j ")

    top_bar = "   "
    i = 0
    char = "x"
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





