from collections import deque
import numpy as np
def read_input():
    with open('day20/input.txt') as file:
        data = {}
        for line in file:
            temp = line.strip()
            temp = temp.split(" -> ")
            if temp[0] == "broadcaster":
                type = 'broadcaster'
                value = 'broadcaster'
            else:
                type = temp[0][0]
                value = temp[0][1:]
            all_input = temp[1].split(", ")
            output = []
            for part in all_input:
                output.append(part)
            data[value] = [type, output, [], "off"]
            output = []
    return data

def press_button(data, q, sum_low, sum_high):
    next = q.popleft()
    print(next)
    # checks if it does not point to anything
    if data.get(next[0]) is not None:
        current = data[next[0]]
        #switch
        if current[0] == "%" and next[1] == "low":
            if current[3] == "off":
                data[next[0]][3] = "on"
                for i in current[1]:
                    q.append([i, "high"])
                    sum_high+=1

            else: 
                data[next[0]][3] = "off"
                for i in current[1]:
                    q.append([i, "low"])
                    sum_low+=1

        # conjunction model
        elif current[0] == "&":
            if len(current[2]) == 1:
                if data[current[2][0]][3] == "on":
                    for i in current[1]:
                        q.append([i, "low"])
                        sum_low +=1
                else:
                    for i in current[1]:
                        q.append([i, "high"])
                        sum_high+=1
            else:
                on = True
                for input in current[2]:
                    if data[input][3] == "off":
                        on = False
                if on:
                    for i in current[1]:
                        q.append([i, "low"])
                        sum_low +=1
                else:
                    for i in current[1]:
                        q.append([i, "high"])
                        sum_high+=1

    return sum_low, sum_high

def Main():
    data = read_input()
    sum_low = 0
    sum_high = 0

    for value in data:
        if value != "broadcaster":
            for x in data[value][1]:
                if data.get(x) is not None:
                    data[x][2].append(value)
    times = 1
    while(times > 0):
        q = deque()
  

        for output in data["broadcaster"][1]:
            q.append([output, "low"])
        
        sum_low = sum_low + len(data["broadcaster"][1])+1

        while(len(q) != 0):
            sum_low, sum_high = press_button(data, q, sum_low, sum_high)
        times-=1
    print(sum_high, sum_low)
    return sum_high * sum_low



print("The final value is: ", Main())