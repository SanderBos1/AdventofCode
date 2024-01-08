
def read_input():
    histories = []
    with open('2023/day9/input.txt') as file:
     for line in file:
            temp = line.strip()
            temp = temp.rsplit(" ")
            print(temp)
            temp = [int(x) for x in temp]
            histories.append(temp)
    return histories



def differences(history_list):
    extrapolate = []
    for i in range(len(history_list)-1):
        difference = history_list[i+1] - history_list[i]
        extrapolate.append(difference)
    return extrapolate, extrapolate[-1]

def history_checker(input):
    total_value = 0
    for line in input:
        values = []
        historyNumber = line[-1]
        while not all(v == 0 for v in line):
            line, value = differences(line)
            values.append(value)
        historyNumber = historyNumber + sum(values)
        total_value = total_value + historyNumber
    return total_value

input = read_input()
solution = history_checker(input)
print("this is the solution: ", solution)
# input = [10,  13,  16,  21,  30,  45 ]
# result, last_result = differences(input)
# print(result)
# print(last_result)