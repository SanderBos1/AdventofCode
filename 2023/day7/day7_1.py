import numpy as np
import pandas as pd

def calculateRank(input):
    rankings = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
    rank = rankings.index(input) + 1
    return rank

def calculateHand(input):
    unique_elements, indices = np.unique(input, return_index = True)
    if(len(indices) == 1):
        return 1
    elif(len(indices) == 2):
        rank = calculate23(input, unique_elements)
        return rank
    elif(len(indices) == 3):
        rank = calculate45(input, unique_elements)
        return rank
    elif(len(indices) == 4):
        return 6
    elif(len(unique_elements) == len(input)):
        return 7


def calculate23(input, unique_elements):
    sumLetters = [0, 0]
    for letter in input:  
        if letter == unique_elements[0]:
            sumLetters[0] = sumLetters[0] + 1
        else:
           sumLetters[1] = sumLetters[1] + 1  
    if sumLetters[0] == 4 or sumLetters[1] == 4:
        return 2
    else:
        return 3
    
def calculate45(input, unique_elements):
    sumLetters = [0, 0, 0]
    for letter in input:  
        if letter == unique_elements[0] or letter == "J":
            sumLetters[0] = sumLetters[0] + 1
        elif  letter == unique_elements[1] or letter == "J":
            sumLetters[1] = sumLetters[1] + 1 
        else:
           sumLetters[2] = sumLetters[2] + 1  
    if sumLetters[0] == 3 or sumLetters[1] == 3 or sumLetters[2] == 3:
        return 4
    else:
        return 5
    
def stringConverter(input):
    letters = []
    for letter in input:
        letters.append(letter)
    return letters


def secondOrdening(input1):
    ranks = []
    for i in range(len(input1)):
        rank1 = calculateRank(input1[i])
        ranks.append(rank1)
    return(ranks)
       


def readInput():
    with open('2023/day7/input.txt') as file:
        cards = []
        for line in file:
            temp = line.strip() 
            split = temp.split(" ")
            split[0] = stringConverter(split[0])
            cards.append(split)
    return cards


cards = readInput()
for card in cards:
    rank = calculateHand(card[0])
    card.append(rank)

    
cards.sort(key = lambda x: x[2])

cards_before = cards.copy()
start = 0
end = -1

for i in range(len(cards_before)):
    cards_before[i] = cards_before[i][1], cards_before[i][2], secondOrdening(cards_before[i][0])


df = pd.DataFrame(cards_before, columns = ["value", "first", "card_values"])
df2 = df[['2','3','4','5','6']] = pd.DataFrame(df.card_values.tolist(), index= df.index)
df = df.drop(["card_values"], axis=1)
print(df)
df= df.sort_values(["first", '2','3','4','5','6'], ascending = False)

print("")
print("")
print("sorted", df)


values = df["value"]
print("")
print(values)
sum = 0
rank = 0
for value in values:
    rank +=1
    sum = sum + int(value) * rank
print(sum)




# print(secondOrdening(['3', '3', '3', '3', '2'], ['7', '7', '7', '8', '8']))
# print(stringConverter("AAAAA"))
# print(calculateRank("1"))
# hand = ["2", "3", "4", "3", "2"]
# print(calculateHand(hand))