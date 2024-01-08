def read_input():
    with open('day19/input.txt') as file:
        Rules = {}
        Parts = []
        consideringRules = True

        for line in file:
            temp = line.strip()
            if temp == "":
                consideringRules = False
            elif consideringRules:
                list_temp = temp.split("{")
                value_list = list_temp[1].replace("}", "").split(",")
                rule = list_temp[0]
                Rules[rule] = value_list
            else:
                temp = temp.replace("{", "").replace("}", "").split(",")
                temp_dict = {}
                for rule in temp:
                    rule = rule.split("=")
                    temp_dict[rule[0]] = int(rule[1])

                
                Parts.append(temp_dict)

                
    return Rules, Parts

def workflowLoop(Rules, part, workflow):
    if workflow == "A" or workflow == "R":
        return workflow
    current = Rules[workflow]
    print(current)
    for i in range(0, len(current)-1):
        system = current[i][0]
        comparator = current[i][1]
        number = int(current[i].split(comparator)[1].split(":")[0])
        next = current[i].split(comparator)[1].split(":")[1]
        if comparator == ">":
            if part[system] > number:
                return next
        else:
            if part[system] < number:   
                return next
    next = current[-1]
    return next


def Main():
    Rules, Parts = read_input()
    sum = 0
    for part in Parts:
        print(part)
        current = 'in'
        while(current != "A" and current != "R"):
            current = workflowLoop(Rules, part, current)
            print(current)
        if current == "A":
            temp_sum = 0
            for value in part:
                temp_sum = temp_sum + part[value]
            sum = sum + temp_sum
    return sum



print("The final answer is: ", Main())