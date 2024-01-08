import numpy as np

def read_input():
    with open('day16/input.txt') as file:
        data = []
        for line in file:
            temp = line.strip()
            temp_data = []
            for character in temp:
                temp_data.append(character)
            data.append(temp_data)
    data = np.array(data)
    return data

def control_beam(value, next, visited_matrix):
    if next == ".":
        visited_matrix[0][value] = True
    elif next == "|":
        print('do i get here')
        for column in range(len(visited_matrix)):
            visited_matrix[column][value] = True
    print(visited_matrix)

   


data = read_input()
visited_matrix = np.full(data.shape, False)
print(visited_matrix)
row = 0
column = 1
direction = "Right"
for i in range(len(data[0])):
    control_beam(i, data[0][i], visited_matrix)
# while(row < len(data) and row >= 0 and column < len(data) and column >=0): 
#     row, column, directon = control_beam(row, column, direction, data[row][column])
#     print(row, column)