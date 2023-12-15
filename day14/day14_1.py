import numpy as np


def readInput():
    data = []
    with open('day14/input.txt') as file:
        for line in file:
            temp = line.strip()
            data.append([x for x in temp])

    data = np.array(data)
    return data

def convert_input(input):
    inputTurned = input

    for i in range(len(inputTurned)):
        for j in range(len(inputTurned[:,i])):
             if(inputTurned[:,i][j]) == "O":
                temp = j-1
                while(temp >-1):
                    if(inputTurned[:,i][temp] == "#"):
                        break
                    else:
                        inputTurned[:,i][temp], inputTurned[:,i][temp+1] = inputTurned[:,i][temp+1], inputTurned[:,i][temp]
                    temp -= 1
    return inputTurned

def readhowmanyO(input):
    sum_rocks = []
    for column in input:
        sum = 0
        for item in column:
            if item == "O":
                sum+=1
        sum_rocks.append(sum)
    return sum_rocks

def calculateTotalLoad(input):
    weight = len(input)
    total_weight = 0
    for i in range(len(input)):
        total_weight = total_weight + input[i]*weight
        weight -= 1
    return total_weight



input = readInput()
converted_input = convert_input(input)
list_howmanyO = readhowmanyO(converted_input)
total_weight = calculateTotalLoad(list_howmanyO)


print("this is total weight", total_weight)