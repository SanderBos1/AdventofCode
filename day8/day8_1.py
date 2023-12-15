import re
import pandas as pd

def readInput():
    with open('day8/input.txt') as file:
        maps = []
        instructions = []
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
                maps.append(temp)
    df = pd.DataFrame(maps, columns=["start", "L", "R"])
    return df, instructions

def loopMaps(maps, current, instruction):
    start = maps.loc[maps['start'] == current]
    # print("this is start", start)
    next = start[instruction].to_string(index=False)
    # print("next", next)
    return next

def mainProgram():
    maps, instructions = readInput()
    print(maps)
    print(instructions)

    next = "AAA"
    print("this is starting point", next)
    sum = 0
    z_found = False
    while(not z_found):
        for instruction in instructions:
            # print("this is instruction", instruction)
            # print("this is next", next)
            sum +=1
            next = loopMaps(maps, next, instruction)
            if next == "ZZZ":
                z_found = True
    print("this is sum", sum)
    return sum
        

mainProgram()


