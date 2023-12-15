
def read_input():
    histories = []
    with open('day9/input.txt') as file:
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
    return extrapolate

def history_checker(input):
    sum = 0
    for line in input:
        values = []
        values.append(line)
        while not all(v == 0 for v in line):
            line = differences(line)
            values.append(line)
        value_after = 0
        for i in reversed(range(0, len(values), 1)):
            value_after =  values[i][0] - value_after
        sum = sum + value_after
    return sum


input = read_input()
solution = history_checker(input)
print("this is the solution: ", solution)
