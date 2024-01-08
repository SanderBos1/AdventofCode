def get_ascii(character):
    ascii_value = ord(character)
    return ascii_value

def increase_17(input):
    output = input * 17
    return output

def remainder(input):
    output = input % 256
    return output

def hascode(input):
    value = 0
    for character in input:
        value = value + get_ascii(character)
        value = increase_17(value)
        value = remainder(value)
    return value

def read_input():
    with open('day15/input.txt') as file:
        for line in file:
            temp = line.strip()
    temp = temp.split(",")
    return temp

def data_to_boxes():
    data = read_input()
    boxes = [{} for i in range(256)]
    for string in data:
        if string[-2] == "=":
            string_split = string.split("=")
            box_number = hascode(string_split[0])
            boxes[box_number].update({string_split[0] : string_split[1]})
        elif string[-1] == "-":
            string_split = string.split("-")
            box_number = hascode(string_split[0])
            if string_split[0] in boxes[box_number]:
                del boxes[box_number][string_split[0]]
    return boxes

def main():
    sum = 0
    boxes = data_to_boxes()
    for box in range(len(boxes)):
        if box == {}:
            sum = sum
        else:
            slot = 0
            for key in boxes[box]:
                slot+=1
                box_number = box + 1
                focal_length = boxes[box][key]
                temp_sum = box_number*int(focal_length)*slot
                sum = sum + temp_sum
    return sum

    

print("The answer of 15_2 is: ", main())


