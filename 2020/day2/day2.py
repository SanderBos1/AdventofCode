def read_file(file_name):
    with open(file_name) as f:
        decoded_lines = []
        lineList =  f.read().splitlines() 
        for line in lineList:
            split_line = line.split(" ")
            numbers = split_line[0].split('-')
            decoded = {
                "low": int(numbers[0]),
                "high":int(numbers[1]),
                "letter": split_line[1][0],
                "password": split_line[2]
            }

            decoded_lines.append(decoded)
    return decoded_lines


def check_password(line, part1):
    sum_number = 0
    if part1:
        for i in line['password']:
            if i == line['letter']:
                sum_number +=1
        if line['low'] <= sum_number <= line['high']:
            return True
        else:
            return False
    else:
        low = line['low'] -1
        high = line['high'] -1

        if line['password'][low] == line['letter'] and line['password'][high]!= line['letter'] or line['password'][high]== line['letter'] and line['password'][low]!= line['letter'] :
            return True
        else:
            return False
    

def passwords_valid(part1):
    sum_valid_passwords = 0
    lines = read_file('2020/day2/input2.txt')
    if part1:
        for i in lines:
            valid = check_password(i, part1)
            if valid:
                sum_valid_passwords += 1
    else:
        for i in lines:
            valid = check_password(i, part1)
            if valid:
                sum_valid_passwords += 1
    return sum_valid_passwords





