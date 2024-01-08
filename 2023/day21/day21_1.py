import numpy as np
from collections import deque

def read_input():
    with open('day21/input.txt') as file:
        data = []
        for line in file:
            temp = line.strip()
            temp_data = []
            for character in temp:
                temp_data.append(character)
            data.append(temp_data)
    data = np.array(data)
    return data

def find_neighbours(data, neighbours, stoped):
    visited = np.full((len(data), len(data[0])), False)

    neighbours_new = []
    for neighbour in neighbours:
        x = neighbour[0]
        y = neighbour[1]
        if x+1 < len(data):
            if data[x+1, y] != "#" and visited[x+1, y] == False:
                neighbours_new.append([x+1, y])
                visited[x+1, y] = True
        if x-1 >= 0:
            if data[x-1, y] != "#"and visited[x-1, y] == False:
                neighbours_new.append([x-1, y])
                visited[x-1, y] = True
        if y+1 < len(data):
            if data[x, y+1] != "#"and visited[x, y+1] == False:
                neighbours_new.append([x, y+1])
                visited[x, y+1] = True
        if y-1 >= 0:
            if data[x, y-1] != "#"and visited[x, y-1] == False:
                neighbours_new.append([x, y-1])
                visited[x, y-1] = True
    return neighbours_new, data, stoped

def draw(data, neighbours):
    for neighbour in neighbours:
        data[neighbour[0]][neighbour[1]] = "O"
    return data

def calculate(data):
    sum = 0
    for x in data:
        for y in x:
            if y == "O":
                sum+=1
    return sum

def Main(steps):
    data = read_input()
    a, b = np.where(data=="S")
    neighbours = [[a[0], b[0]]]
    stoped = []

    while steps > 0:
        neighbours, data, stoped = find_neighbours(data,neighbours, stoped)
        steps-=1

    data = draw(data, neighbours)

    data = draw(data, stoped)
    sum = calculate(data)

    return sum


print("Final answer is : ", Main(64))