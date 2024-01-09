import numpy as np

def readInput():
    data = []
    with open('2023/day14/input.txt') as file:
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



def calculateTotalLoad(input):
    total_weight = 0
    for i in range(len(input)):
        for j in range(len(input[0])):
            weight = len(input)-i
            if input[i, j] == "O":
                total_weight = total_weight+weight
    return total_weight



input = readInput()
converted_input = convert_input(input)
total_weight = calculateTotalLoad(converted_input)


print("this is total weight", total_weight)