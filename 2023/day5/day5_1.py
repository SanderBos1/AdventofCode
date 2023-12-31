
def readInput():


    with open('2023/day5/input.txt') as file:
        important = []
        lines = []
        for line in file:
            temp = line.strip()
            if(temp == ""):
                important.append(lines)
                lines = []
            else:
                lines.append(temp)
    important.append(lines)
    return important
           
def converter(input):
    if(len(input) == 1):
        input[0] = input[0].replace('seeds: ', '')
    else:
        del input[0]
    for i in range(len(input)):
        temp = input[i].split()
        input[i] = [int(x) for x in temp]
    return input

def determine(seeds, nextLine):
    for tuple in nextLine:
        destination = tuple[0]
        source = tuple[1]
        steps = tuple[2]
        if(source <= seeds < source+steps):
                seeds =  seeds - source + destination
                break

    return seeds

def toSeed(seeds):

    seeds_replacement = []

    for i in range(0, len(seeds)):
        seeds_replacement.append(seeds[i])

    return seeds_replacement

def main():
    input = readInput()
    seeds = converter(input[0])[0]
    del input[0]
    seeds = toSeed(seeds)
    
    for i in range(0, len(input)):
        input[i] = converter(input[i])

    min = 0
    for seed in seeds:
        step_between = seed
        for i in range(len(input)):
            step_between = determine(step_between, input[i])
        if(min == 0):
            min = step_between
        elif(min > step_between):
            min = step_between
    
    print("final solution : ", min)
        

  

        

main()

