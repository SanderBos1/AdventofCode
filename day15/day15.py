def get_ascii(character):
    ascii_value = ord(character)
    return ascii_value

def increase_17(input):
    output = input * 17
    return output

def remainder(input):
    output = input % 256
    return output

def hascode(input, current_value):
    current_value = current_value + get_ascii(input)
    current_value = increase_17(current_value)
    current_value = remainder(current_value)
    return current_value

def read_input():
    with open('day15/input.txt') as file:
        for line in file:
            temp = line.strip()
    temp = temp.split(",")
    return temp

def main():
    data = read_input()
    print(data)
    sum = 0
    for string in data:
        print(string)
        temp_sum = 0
        for character in string:
            temp_sum = hascode(character, temp_sum)
        sum = sum + temp_sum
    return sum

print("The answer of 15_1 is: ", main())