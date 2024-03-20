def read_file(file_name):
    with open(file_name) as f:
        numbers = []
        for line in f:
            number = int(line)
            numbers.append(number)
    return numbers



def summation():
    list_of_numbers = read_file('2020/input1.txt')
    for i in range(len(list_of_numbers)):
        for j in range(i+1, len(list_of_numbers)):
            if(list_of_numbers[i] + list_of_numbers[j] == 2020):
                return list_of_numbers[i] * list_of_numbers[j]


def summation_2():
    list_of_numbers = read_file('2020/input1_2.txt')
    for i in range(len(list_of_numbers)):
        for j in range(i+1, len(list_of_numbers)):
            for k in range(i+2, len(list_of_numbers)):
                if(list_of_numbers[i] + list_of_numbers[j] + list_of_numbers[k] == 2020):
                    return list_of_numbers[i] * list_of_numbers[j]* list_of_numbers[k]
