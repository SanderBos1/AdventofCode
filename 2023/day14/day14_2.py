import numpy as np




def readInput():
    data = []
    with open('day14/input.txt') as file:
        for line in file:
            temp = line.strip()
            data.append([x for x in temp])

    data = np.array(data)
    return data

def convert_input_north(input):
    for i in range(len(input)):
        for j in range(len(input[:,i])):
             if(input[:,i][j]) == "O":
                temp = j-1
                while(temp >-1):
                    if(input[:,i][temp] == "#"):
                        break
                    else:
                        input[:,i][temp], input[:,i][temp+1] = input[:,i][temp+1], input[:,i][temp]
                    temp -= 1
    return input


def convert_input_south(input):
    # print("this is input")
    # print(input)
    temp = 0
    for i in range(len(input)):
        # print(inputTurned[:,i])
        for j in range(len(input[:,i])):
            if(input[:,i][j]== "O"):
                input[:,i][j] = "."
                temp +=1
            if(input[:,i][j] == "#"):
                # print("")
                # print(input[:,i], temp)
                # print("")

                while(temp > 0):
                    input[:,i][j-temp] = "O"
                    temp-=1
                # print(input[:,i], temp)
                # print("")
            if(j == len(input[:,i])-1):
                temp-=1
                while(temp > -1):
                    input[:,i][j-temp] = "O"
                    temp-=1
                temp = 0
    return input

def convert_input_east(input):
    count = 0
    for i in range(len(input)):

        for j in range(len(input[i])):
            if input[i][j] == "O":
                count +=1
                input[i][j] = "."
            if input[i][j] == "#" or j == len(input[i])-1:
                start_left = i
                if input[i][j] == "#":
                    start_right = j-1
                else:
                    start_right = j
                while(count > 0):
                    input[start_left][start_right] = "O"
                    start_right -=1
                    count -=1
                count = 0
    return input

def convert_input_west(input):
    count = 0
    for i in range(len(input)):
        start_left = i
        start_right = 0
        for j in range(len(input[i])):
            if input[i][j] == "O":
                count +=1
                input[i][j] = "."
            if input[i][j] == "#" or j == len(input[i])-1:
                while(count > 0):
                    input[start_left][start_right] = "O"
                    start_right +=1
                    count -=1
                start_left = i
                start_right = j+1
                count = 0
    return input

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

def convertCycle(input, cycles):
    while(cycles > 0):
        input = convert_input_north(input)
        input = convert_input_west(input)
        input = convert_input_south(input)
        input = convert_input_east(input)
        cycles -=1
    return input

input = readInput()
print("this was input")
print(input)
converted_input = convertCycle(input, 1000)
converted_input = convert_input_east(input)
print("this is the converted input")
print(converted_input)
list_howmanyO = readhowmanyO(converted_input)
total_weight = calculateTotalLoad(list_howmanyO)

#north is correct
#South is correct
#west is correct
#east is correct
print(list_howmanyO)
print(total_weight)