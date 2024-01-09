import numpy as np
import math

def read_input():
    with open('2023/day10/input.txt') as file:
        data = []
        for line in file:
            temp = line.strip()
            temp_data = []
            for character in temp:
                temp_data.append(character)
            data.append(temp_data)
    data = np.array(data)
    return data


def find_value_S(s_position, data):
        
        check = []
        right = [s_position[0], s_position[1]+1]
        left = [s_position[0], s_position[1]-1]
        down = [s_position[0]+1, s_position[1]]
        up = [s_position[0]-1, s_position[1]]

        if data[left[0], left[1]] in ["-", "F", "L"]:
            check.append("left")
        if data[right[0], right[1]] in ["-", "7", "J"]:
            check.append("right")
        if data[down[0], down[1]] in ["|", "L", "J"]:
            check.append("down")
        if data[up[0], up[1]] in ["|", "F", "7"]:
            check.append("up")
        
        if "left" in check and "right" in check:
            return "-"
        elif "up" in check and "right" in check:
            return "L"
        elif "down" in check and "right" in check:
            return "F"
        elif "left" in check and "up" in check:
            return "J"
        elif "left" in check and "down" in check:
            return "7"
        else:
            return "|"
        
def shoelace(list_vertices):
    holder = 0
    for pair in range(len(list_vertices)-1):
        holder = holder + list_vertices[pair][0] * list_vertices[pair+1][1] - list_vertices[pair][1] * list_vertices[pair+1][0]
    holder = holder + list_vertices[-1][0] * list_vertices[0][1] - list_vertices[-1][1] * list_vertices[0][0]
    return abs(holder)/2
        
def Main():
    data = read_input()
    s_position = [x[0] for x in  np.where(data=="S")]
    bends = ["F", "J", "L", "7"]

    pipes = {
        "|": {(1, 0): (1, 0), (-1, 0): (-1, 0)},
        "-": {(0, 1): (0, 1), (0, -1): (0, -1)},
        "L": {(1, 0): (0, 1), (0, -1): (-1, 0)},
        "J": {(0, 1): (-1, 0), (1, 0): (0, -1)},
        "F": {(-1, 0): (0, 1), (0, -1): (1, 0)},
        "7": {(0, 1): (1, 0), (-1, 0): (0, -1)},
    }

    borders = 1
    V = [s_position]
    stepx, stepy = 0, 1

    x = s_position[0] 
    y = s_position[1]

    x = x + stepx
    y = y + stepy
    step = 1
    value = data[x, y]

    while(value != "S"):


        pipe = pipes[value]
        stepx, stepy = pipe[stepx, stepy]

        x = x + stepx
        y = y + stepy
        value = data[x, y]
        if value in bends:
            borders += 1
            V.append([x, y])
        step+=1

    Area = math.floor(shoelace(V))
    Enclosed = Area - step/2 +1
    return Enclosed

# vertices = [(1,6), (3, 1), (7, 2), (4, 4), (8, 5)]
# print(shoelace(vertices))
print("The final answer is : ", Main())