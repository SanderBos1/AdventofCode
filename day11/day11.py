import numpy as np
from itertools import combinations

def read_input():
    data = []
    with open('day11/input.txt') as file:
        for line in file:
            temp = line.strip()
            data.append([x for x in temp])

    numberUniverse = 0
    for i in range(len(data)):
        for point in range(len(data[i])):
            if data[i][point] == "#":
                data[i][point] = int(numberUniverse)
                numberUniverse+=1
    return data, numberUniverse

def distance_coordinates(pair, converted_data, empty_universes_row, empty_universes_column, weight):
    a = str(pair[0])
    b = str(pair[1])
    i, j = np.where(converted_data==a)
    k, l = np.where(converted_data==b)
    reverse = False
    reverseColumn = False
    if k < i:
        reverse = True
    if l < j:
        reverseColumn = True

    sum_row = 0
    sum_column = 0
    if(not reverse):
        for number in range(int(i), int(k), 1):
            if number in empty_universes_row:
                sum_row = sum_row + 1*weight
            else: sum_row +=1
    else:
         for number in range(int(i), int(k), -1):
            if number in empty_universes_row:
                sum_row = sum_row + 1*weight
            else: sum_row +=1     

    if(not reverseColumn):
        for column_number in range(int(j), int(l), 1):
            if column_number in empty_universes_column:
                sum_column = sum_column + 1*weight
            else:
                sum_column +=1
    else:
        for column_number in range(int(l), int(j), 1):
            if column_number in empty_universes_column:
                sum_column = sum_column + 1*weight
            else:
                sum_column +=1

    difference = sum_row + sum_column
    return difference

def sum_distances(converted_data, numberUniverse, empty_universes_row, empty_universes_column, weight):
    total = 0
    numberlist = [*range(0, numberUniverse, 1)]
    distances = combinations(numberlist, r=2)
    for pair in distances:
        distance = distance_coordinates(pair, converted_data, empty_universes_row, empty_universes_column, weight)
        total = total + distance
    return total


def check_contains_digit(values):
    for value in values:
        if value.isdigit():
            return True
    return False


def main(weight):
    converted_data, numberUniverse = read_input()
    converted_data = np.array(converted_data)

    empty_universes_row = []
    for row in range(len(converted_data)) :
        if(not check_contains_digit(converted_data[row])):
            empty_universes_row.append(row)

    empty_universes_column = []
    reversed = converted_data.T
    for row in range(len(reversed)) :
        if(not check_contains_digit(reversed[row])):
            empty_universes_column.append(row)

    final_value = sum_distances(converted_data, numberUniverse, empty_universes_row, empty_universes_column, weight)
    return final_value


print("this is final value: ", main(2))


