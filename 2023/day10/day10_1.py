import numpy as np
from collections import deque

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

def queue_logic(data, visited, distance, values, q):
    both = q.popleft()
    current = both[0]
    current_value = both[1]

    if current[0] >= 0 and current[0] < len(data) and current[1] >=0 and current[1] < len(data[0]):
    
        right = [current[0], current[1]+1]
        left = [current[0], current[1]-1]
        down = [current[0]+1, current[1]]
        up = [current[0]-1, current[1]]
        
        if current_value in ["F", "7" ,"|"]:
            if visited[down[0], down[1]] == False:
                q.append([down, data[down[0], down[1]]])
                visited[down[0], down[1]] = True
                distance[down[0], down[1]] = distance[current[0], current[1]] +1
                values[down[0], down[1]] = current_value
        if current_value in ["J", "L", "|"]:
            if visited[up[0], up[1]] == False:
                q.append([up, data[up[0], up[1]]])
                visited[up[0], up[1]] = True
                distance[up[0], up[1]] = distance[current[0], current[1]] +1
                values[up[0], up[1]] = current_value

        if current_value in ["7", "J" ,"-"]:
            if visited[left[0], left[1]] == False:
                q.append([left, data[left[0], left[1]]])
                visited[left[0], left[1]] = True
                distance[left[0], left[1]] = distance[current[0], current[1]] +1
                values[left[0], left[1]] = current_value

        if current_value in ["L", "F", "-"]:
            if visited[right[0], right[1]] == False:
                q.append([right, data[right[0], right[1]]])
                visited[right[0], right[1]] = True
                distance[right[0], right[1]] = distance[current[0], current[1]] +1
                values[right[0], right[1]] = current_value

  
    return data, visited, distance,values,  q

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
        
                

        
def Main():
    data = read_input()
    row = len(data)
    column = len(data[0])
    s_position = [x[0] for x in  np.where(data=="S")]

    visited = np.full((row, column), False)
    distance = np.matrix(np.zeros((row, column)))
    values = np.matrix(np.chararray((row, column)))
    values[:] = "O"
    s_value = find_value_S(s_position, data)

    visited[s_position[0], s_position[1]] = True
    distance[s_position[0], s_position[1]] = 0
    values[s_position[0], s_position[1]] = s_value
    
    print(s_value)

    q = deque()
    q.append([s_position, s_value])
    while(len(q) != 0):
        data, visited, distance, values, q = queue_logic(data, visited, distance, values, q)
    print(values)

    return distance


print("The final answer is : ", int(np.max(Main())))