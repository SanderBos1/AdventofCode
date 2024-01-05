import re

def read_input():
    with open('day5/input.txt') as file:
        seeds = []
        mappings = []
        temp_mappings = []
        for count, line in enumerate(file):
            if count == 0:
                seeds=re.findall(r"\d+", line)
                seeds = [int(x) for x in seeds]
                real_seeds = []
                for i in range(0, len(seeds)-1, 2):
                    seeds[i+1] = seeds[i+1] + seeds[i]
                    real_seeds.append([seeds[i], seeds[i+1]])
            elif line not in ['\n', '\r\n']:
                mapping = re.findall(r"\d+", line)
                if mapping != []:
                    mapping = [int(x) for x in mapping]
                    temp_mappings.append(mapping)
            else:
                if temp_mappings != []:
                    mappings.append(temp_mappings)
                    temp_mappings = []
    mappings.append(temp_mappings)
    return real_seeds, mappings
            
                
def convert_range(mappings, pair, answer):
    for rule in mappings:
        destination = rule[0]
        source = rule[1]
        mapping_range = rule[2]
        source_end = source + mapping_range -1
        difference = destination - source
        start, end = pair[0], pair[1]
        if source <= start and end <= source_end:
            answer.append([start + difference, end + difference])
            return answer
        elif source > start and source < end and end <= source_end:
            answer.append([destination, end + difference])
            step = convert_range(mappings, [start, source-1], answer)
            for i in step:
                if i not in answer:
                    answer.append(step)
            return answer
        elif start >= source and start <= source_end and  end > source_end:
            answer.append([start + difference, source_end + difference])
            step = convert_range(mappings, [source_end + 1, end], answer)
            for i in step:
                if i not in answer:
                    answer.append(step)
            return answer
    answer.append(pair)
    return answer

def Main():
    minimum = float("inf")
    seeds, mappings = read_input()
    while seeds != []:
        converted_pair = [seeds.pop()]
        for mapping in mappings:
            temp_pair_list = []
            for pair in converted_pair:
                answer = []
                temp_pair_list.extend(convert_range(mapping, pair, answer))
            converted_pair = temp_pair_list.copy()
        for item in converted_pair:
            if item[0] < minimum:
                minimum = item[0] 
    return minimum


print("The final answer is: ", Main())