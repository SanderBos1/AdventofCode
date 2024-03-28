import numpy as np

def read_file(file, repeats):
    r = open(file).read().strip('\n')
    matrix = []
    new_line = ''
    input = r.splitlines()
    for line in input:
        for _ in range(repeats):
            new_line = new_line + line
        matrix.append(new_line)
        new_line = ''
    matrix = np.array(matrix)
    return matrix



def check_tree(position, encountered, matrix, step_x, step_y):
    position_x = position[0] + step_x
    position_y = position[1] + step_y
    if matrix[position_y][position_x] == "#":
        encountered += 1
    
    return [position_x, position_y], encountered


def check_length(step_right):
    file = '2020/day3/input3.txt'
    r = open(file).read().strip('\n')
    input = r.splitlines()
    input = np.array(input)
    length = len(input)
    width = len(input[0])
    width = int((step_right*length)/width + 1)
    return length, width


def part1_solution():
    length, width = check_length(3)
    file = '2020/day3/input3.txt'
    encountered = 0
    position = [0, 0]
    matrix = read_file(file, width)
    while(position[1] < length-1):
        position, encountered = check_tree(position, encountered, matrix, 3, 1)
    return encountered


def part2_solution():
    file = '2020/day3/input3.txt'
    positions = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    encountered_sum = 1
    for position in positions:
        length, width = check_length(position[0])
        encountered = 0
        start = [0, 0]
        matrix = read_file(file, width)
        while(start[1] < length-1):
            start, encountered = check_tree(start, encountered, matrix, position[0], position[1])
        encountered_sum = encountered_sum *  encountered
    return encountered_sum

part2_solution()