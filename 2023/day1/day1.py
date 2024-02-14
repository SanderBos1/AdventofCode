import re

def day1_1():
    with open('2023/day1/input.txt', encoding="utf-8") as file:
        value_sum = 0
        for line in file:
            line = re.findall(r"\d", line)
            calibration_value = line[0]+line[-1]
            value = int(calibration_value)
            value_sum = value_sum + value
    return value_sum

def day1_2():

    with open('2023/day1/input.txt', encoding="utf-8") as file:
        value_sum = 0
        #need first and last letter with letters that can be combined
        help_dictionary  = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "4",
        "five": "5e",
        "six": "6",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e",
}
        for line in file:
            for k, v in help_dictionary.items():
                line = line.replace(k, v)
            line = re.findall(r"\d", line)
            calibration_value = line[0]+line[-1]
            value = int(calibration_value)
            value_sum = value_sum + value
    return value_sum


print("Answer of part 1 is: ", day1_1())
print("Answer of part 2 is: ", day1_2())
