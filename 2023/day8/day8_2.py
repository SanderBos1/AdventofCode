import re
import pandas as pd
import numpy as np
from math import gcd

def readInput():
    with open('2023/day8/input.txt') as file:
        maps = []
        instructions = []
        begin = []
        skip = True
        for line in file:
            temp = line.strip()
            if(skip):
                if temp == "":
                    skip = False
                else:
                    instructions.extend(temp)
            else:
                temp = re.split(r'[\W+]', temp)
                temp = list(filter(None, temp))
                if temp[0][2] == "A":
                    begin.append(temp[0])
                maps.append(temp)
    df = pd.DataFrame(maps, columns=["start", "L", "R"])
    return df, instructions, begin

def loopMaps(maps, current, instruction):
    start = maps.loc[maps['start'] == current]
    next = start[instruction].to_string(index=False)
    return next

def mainProgram(maps, instructions, next):
    sum = 0
    z_found = False
    while(not z_found):
        for instruction in instructions:
            # print("this is instruction", instruction)
            # print("this is next", next)
            sum +=1
            next = loopMaps(maps, next, instruction)
            if next[2] == "Z":
                sum = sum
                z_found = True
                break
    print("this is sum", sum)
    return sum
        

maps, instructions, begin = readInput()

sums = []
for start in begin:
    sum = mainProgram(maps, instructions, start)
    sums.append(sum)

sums = np.array(sums)
print(sums)
lcm = 1
for i in sums:
    lcm = lcm*i//gcd(lcm, i)
print(lcm)