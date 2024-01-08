import math

def read_input():
    with open('day19/input.txt') as file:
        Rules = {}
        for line in file:
            temp = line.strip()
            if temp == "":
                return Rules
            list_temp = temp.split("{")
            value_list = list_temp[1].replace("}", "").split(",")
            rule = list_temp[0]
            Rules[rule] = value_list
    return Rules

def workflowLoop(possible_ranges, Rules, good_Ranges):
    new_possible_range = []

    for possible_range in possible_ranges:
        # print(possible_range)
        Intact_ranges = possible_range[0].copy()
        updated_ranges = possible_range[0].copy()
        if possible_range[1] != "A" and possible_range[1] != "R":
            rule = Rules[possible_range[1]]
            for i in range(len(rule)-1):
                system = rule[i][0]
                comparator = rule[i][1]
                number = int(rule[i].split(comparator)[1].split(":")[0])
                next = rule[i].split(comparator)[1].split(":")[1]
                # print("this is system: ", system)
                # print("this is comparator: ", comparator)
                # print("this is number: ", number)
                # print("this is next: ", next)
                if comparator == ">":
                    updated_ranges.update({system:[number, 4000]})
                    if next == "A":
                        if [updated_ranges, next] not in good_Ranges:
                            good_Ranges.append(updated_ranges)
                    elif next != "R":
                        new_possible_range.append([updated_ranges, next])
                        Intact_ranges.update({system:[1, number-1]})

                else:
                    updated_ranges.update({system:[1, number-1]})
                    if next == "A":
                        if [updated_ranges, next] not in good_Ranges:
                            good_Ranges.append(updated_ranges)
                    elif next != "R":
                        new_possible_range.append([updated_ranges, next])
                        Intact_ranges.update({system:[number, 4000]})
                
                new_possible_range.append([Intact_ranges, rule[-1]])

    return new_possible_range, good_Ranges

def clean_ranges(good_Ranges):
    new_good_ranges = []
    for goodRange in good_Ranges:
        print("this is goodRange now")
        print(goodRange)
        print("")
        if new_good_ranges == []:
            new_good_ranges.append(goodRange)
        else:
            skip = False
            for j in range(len(new_good_ranges)):
                for i in range(len(goodRange)):
                    if goodRange[i][0] >=  new_good_ranges[j][i][0] and goodRange[i][1] <=  new_good_ranges[j][i][1]:
                        pass
                    elif goodRange[i][0] <=  new_good_ranges[j][i][0] and goodRange[i][1] >=  new_good_ranges[j][i][1]:
                        new_good_ranges.append(goodRange)
                        skip = True
                        break
                if skip:
                    break
        print(new_good_ranges)
        print("")

    print("this is new", new_good_ranges)

def Main():
    Rules = read_input()
    Ranges = {"x": [1, 4000],
              "m": [1, 4000],
              "a": [1, 4000],
              "s": [1, 4000]
              }
    possible_ranges = [[Ranges, "in"]]
    hasChanged = True
    next = possible_ranges
    good_Ranges = []
    while(hasChanged):
        old_next = next.copy()
        next, good_Ranges = workflowLoop(next, Rules, good_Ranges)
        if old_next == next:
            hasChanged = False

    #convert for easy access
    new_good_Ranges = []
    for dictionary in good_Ranges:
        temp = []
        for value in dictionary:
            temp.append(dictionary[value])
        new_good_Ranges.append(temp)
    new_good_Ranges = clean_ranges(new_good_Ranges)



print("The final answer is: ", Main())
