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

def Main(cycle):
    board_states_seen = {}
    input = readInput()
    loadings = [None]
    current_cycle = 0
    while True:

        for i in range(4):
            input = convert_input(input)
            input = np.rot90(input, 3)

        answer = calculateTotalLoad(input)
        loadings.append(answer)
        board_state = "".join(["".join(row) for row in input])
        current_cycle += 1

        if board_state in board_states_seen:
            end_cycle = current_cycle
            start_cycle = board_states_seen[board_state]
            loop_size = end_cycle - start_cycle
            final_cycle_match = (( cycle - start_cycle) % loop_size) + start_cycle
            answer = loadings[final_cycle_match]
            return answer
        else:
            board_states_seen[board_state] = current_cycle



print("The final answer is: ", Main(1000000000))
