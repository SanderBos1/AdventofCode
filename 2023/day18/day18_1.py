import numpy as np

def read_input():
    with open('day18/input.txt') as file:
        data = []
        for line in file:
            temp = line.strip()
            list_temp = temp.split(" ")
            list_temp[1] = int(list_temp[1])
            data.append(list_temp)
    return data

def dig_right(matrix, depth, column, row):
    if len(matrix)==0:
        column = depth-1
        temp = ["#"] * depth
        matrix.append(temp)
    else:
        difference = column + depth - len(matrix[row])+1
        while difference > 0:
            difference-=1
            for item in matrix:
                item.append(".")
        for i in range(depth):
            column+=1
            matrix[row][column] = "#"
    
    # print("matrix after right")
    # print(matrix)
    # print(row, column)
    # print("")
    return matrix, column, row

def dig_left(matrix, depth, column, row):
    difference = column - depth
    while difference < 0:
        for item in matrix:
            item.insert(0, ".")
        column+=1
        difference+=1
    for i in range(depth):
        column-=1
        matrix[row][column] = "#"
    # print("matrix after left")
    # print(matrix)
    # print(row, column)
    # print("")
    return matrix, column, row

def dig_down(matrix, depth, column, row):
    difference = row + depth
    size = len(matrix)
    # print("this is difference", difference)
    while difference > size-1:
        temp = ["."]*len(matrix[0])
        matrix.append(temp)
        difference-=1
    new_row = row+depth
    for i in range(row, new_row+1, 1):
        matrix[i][column] = "#"
    row = new_row
    # print("matrix after down")
    # print(matrix)
    # print(row, column)
    # print("")
    return matrix, column, row

def dig_up(matrix, depth, column, row):
    difference = row - depth
    print(row, column)
    print("this is difference", difference)
    if difference < 0:
        while difference < 0:
            temp = ["."]*len(matrix[0])
            temp[column] = "#"
            matrix.insert(0, temp)
            difference+=1
        row = 0
    elif(difference >= 0):
        for i in range(row, row-depth-1, -1):
            print(i)
            matrix[i][column] = "#"
        row = row-depth
    # print("matrix after up")
    # print(matrix)
    # print(row, column)
    # print("")
    return matrix, column, row

def digging(matrix, input):
    column = 0
    row = 0
    for line in input:
        print("this is line", line)
        print(" ")
        if line[0] == "R":
            matrix, column, row = dig_right(matrix, line[1], column, row)
        elif line[0] == "L":
            matrix, column, row = dig_left(matrix, line[1], column, row)
        elif line[0] == "D":
            matrix, column, row = dig_down(matrix, line[1], column, row)
        else:
            matrix, column, row = dig_up(matrix, line[1], column, row)


    return matrix

def fill_array(input):
    for line in input:
        for i in range(len(line)-1):
            if line[i] == "#":
                for j in range(i+1, len(line), 1):
                    if line[j] == "#":
                        for k in range(i, j, 1):
                            line[k] = "#"
                        i = j
    return input


def Main():
    data = read_input()
    data_matrix = []
    data_matrix = digging(data_matrix, data)
    data_matrix =  fill_array(data_matrix)
    print(data_matrix)
    sum = 0
    for line in data_matrix:
        for value in line:
            if value == "#":
                sum+=1
    return sum




print("The final answer is: ", Main())