import re

def hold_time(time, hold_time):
    time = time-hold_time
    distance = hold_time * time
    return distance


def options(record, record_distance):
    print(record, record_distance)
    sum = 0
    for holdTime in range(1, record):
        traveled = hold_time(record, holdTime)
        if traveled > record_distance:
            sum = sum+1
    return sum


def ways_beat_record(races, distances):
    sum = 1
    for i in range(len(races)):
        print(i)
        race = races[i]
        distance = distances[i]
        option = options(race, distance)
        sum = sum * option
    return sum

def readInput():
    with open('2023/day6/input.txt') as file:
        all = []
        for line in file:
            temp = line.strip()
            temp = re.findall(r'[0-9]+', temp)
            giantString = ""
            for number in temp:
                giantString = giantString + number
            
            all.append([int(giantString)])
            giantString = ""

    return all


b = readInput()
a = ways_beat_record(b[0], b[1])
print("this is a", a)