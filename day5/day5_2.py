import re

def readInput():


    with open('day5/input.txt') as file:
        important = []
        lines = []
        for line in file:
            read_line = line.strip()
            if(read_line != ""):
                read_line_filtered = re.findall(r'[0-9]+',read_line)
                read_line_int = [eval(i) for i in read_line_filtered]
                if(len(read_line_int)>1):
                    lines.append(read_line_int)
            else:
                important.append(lines)
                lines = []
    return important


#converts seeds to ranges
def dataPrep(input):
    seeds = input[0][0].copy()
    input.remove(input[0])
    range_seeds = []
    for seed in range(0, len(seeds)-1, 2):
        print(seed)
        end = seeds[seed]+seeds[seed+1]-1
        range_seeds.append([seeds[seed], end])


    return range_seeds, input

def decoding(seeds, refactor):
    
    still_check = []
    destination = refactor[0]
    source = refactor[1]
    step = refactor[2]-1
    # print("Destination ", refactor[0], "Source", refactor[1], "step", refactor[2])
    if(seeds[0] >= source and seeds[1] <= source+step):
        # print("both in range")
        seeds[0] = seeds[0] - source + destination
        seeds[1] = seeds[1] - source + destination
        return[seeds[0], seeds[1]], still_check
    #left side of range is outside right is inside
    elif(seeds[0] < source and seeds[1] < source+step and seeds[1] > source):
        # print("left in range, right outside")
        convert_code = destination - source
        border_right = source 
        border_left = border_right-1
        border_right = border_right + convert_code
        seeds[1] = seeds[1] + convert_code
        still_check.append([seeds[0], border_left])
        # print(seeds[0], border_left, border_right, seeds[1])
        return [border_right, seeds[1]], still_check
    
    #left side is in range and rightside is outside
    elif(seeds[0] > source and seeds[0] < source+step+1 and seeds[1] >= source+step):
        # print("left out of range, right inside")
        convert_code = destination-source
        seeds[0] = seeds[0] + convert_code
        border_left = source+step
        border_right = source + step + 1
        border_left = border_left + convert_code
        still_check.append([border_right, seeds[1]])
        # print("this is still check", still_check)
        # print(seeds[0], border_left, border_right, seeds[0])
        return [seeds[0], border_left], still_check
    return[seeds[0], seeds[1]], still_check

    

def main():
    input = readInput()
    seeds, codeRefactor = dataPrep(input)
    for seed in seeds:
        print("this is the beginning", seed)
        for code in codeRefactor:
            print("next")
            print("")
    
          



seed = [79, 99]
line = [52, 50, 48]
def test(seed, line):
    converted, check = decoding(seed, line)
    print("this is converted", converted)
    print("this is check" ,check)
    if(check == []):
        print(converted)
    else:
        new = test(check[0], line)
        print("this is new", new)
        converted.append(new)
    return converted
print(test(seed, line))