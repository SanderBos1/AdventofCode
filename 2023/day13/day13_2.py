import numpy as np
import collections

def read_input():
    with open('day13/input.txt') as file:
        data = []
        all_data = []
        for line in file:
            temp = line.strip()
            if temp == "":
                all_data.append(data)
                data = []
            else:
                data.append([x for x in temp])
    all_data.append(data)
    return all_data

def check_equal(lista, listb):
    for i in range(len(lista)):
        if lista[i] != listb[i]:
            return False
    return True

def check_mirror(input):

    #columns
    for i in range(input.shape[1]-1):
        first = input[:,i]
        second = input[:,i+1]
        if(check_equal(first, second)):
            left = i-1
            right = i+2
            mirror = True
            while(left >= 0 and right < input.shape[1]):
                first =input[:,left]
                second =input[:,right]
                if(not check_equal(first, second)):
                    mirror = False
                    break
                left -= 1
                right+=1
            if(mirror):
                number = i+1
                return number
            

    for i in range(len(input)-1):
        first = input[i]
        second = input[i+1]
        if(check_equal(first, second)):
            left = i-1
            right = i+2
            mirror = True
            while(left >= 0 and right < len(input)):
                first =input[left]
                second =input[right]
                if(not check_equal(first, second)):
                    mirror = False
                    break
                left -= 1
                right+=1
                print(right, len(input[i]))
            if(mirror):
                print(i, i+1)
                number = i+1
                return number*100

def main():
    sum = 0
    input = read_input()
    for mirror in input:
        temp = np.array(mirror)
        print(temp)
        sum = sum + check_mirror(temp)
    return sum
print("the final solution is: ", main())



