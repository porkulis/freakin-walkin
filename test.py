import sys
import os
clear = lambda: os.system('cls')

grid = []
col = []
row = []

i = 0
for n in range(10):
    row.append(i)
    i += 1

i = 0
for n in range(10):
    col.append(i)
    i += 1

col = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

grid.append(col)
grid.append(row)

def get_direction():
    location_change = [0 ,0]
    dir = input("Kierunek: ")
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
    blank = " . "
    line = ""
    empty_line = blank * 10
    for n in grid[0]:
        if n == current_location[0]:
            line += " █ "
        else:
            line += blank
    #print("Sterowanie: wsad + Enter. \"Q\" by wyjść.\n")
    print("    a  b  c  d  e  f  g  h  i  j ")
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
    print(f"{current_location[0]}")
    print(f"{current_location[1]}")


indexes = [0, 0]
current_location = grid[0][indexes[0]], grid[1][indexes[1]]
print(current_location)
display_map()

zmiana = []
while True:
    zmiana = get_direction()
    if indexes[0] < 9:
        if zmiana[0] < 1:
            indexes[0] += zmiana[0]
    else:
        indexes[0] += zmiana[0]
    if indexes[1] < 9:
        if zmiana[1] < 1:
            indexes[1] += zmiana[1]
    else:
        indexes[1] += zmiana[1]

    print(f"len x: {len(grid[0])}")
    print(f"len y: {len(grid[1])}")
    print(f"x: {indexes[0]}")
    print(f"y: {indexes[1]}")
    current_location = grid[0][indexes[0]], grid[1][indexes[1]]

    print(current_location)
    display_map()
    print(f"indexes: {indexes}")
    print(f"Zmiana: {zmiana}")





