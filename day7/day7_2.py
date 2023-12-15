import numpy as np
import pandas as pd

def calculateRank(input):
    rankings = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
    rank = rankings.index(input) + 1
    return rank

def readInput():
    with open('day7/input.txt') as file:
        cards = []
        for line in file:
            temp = line.strip() 
            split = temp.split(" ")
            hand_converted = []
            for character in split[0]:
                character = calculateRank(character)
                hand_converted.append(character)
            cards.append([ split[1], split[0], hand_converted])
    df = pd.DataFrame(cards, columns  = ["Number", "Hand",  "Hand_converted"])
    df2 = df[['card1','card2', 'card3', 'card4', 'card5']] = pd.DataFrame(df.Hand_converted.tolist(), index= df.index)
    df = df.drop("Hand_converted", axis=1)
    df = df.assign(rank = 0)
    return df

def readRank(input):
    max = 0
    for character in input:
        temp_max = 0
        for character_2 in input:
            if character == character_2 or character_2 == "J":
                temp_max +=1
        if temp_max > max:
            max = temp_max
    if max == 2 or max == 3:
        return unique_values(input, max)
    return max

def unique_values(input, max):
    unqiue_characters = []
    for character in input:
        if character not in unqiue_characters and character != "J":
            unqiue_characters.append(character)
    if len(unqiue_characters) == 2:
        return "Full house"
    elif len(unqiue_characters) == 3 and max == 3:
        return "Three of a kind"
    if len(unqiue_characters) == 4:
        return "One pair"
    elif len(unqiue_characters) == 3 and max == 2:
        return "Two pair"


dictRanking = {
    5 : 1,
    4 : 2,
    "Full house": 3,
    "Three of a kind" : 4,
    "Two pair" : 5,
    "One pair" : 6,
    1 : 7
}


df = readInput()
df["rank"] = df['Hand'].apply(lambda x: dictRanking[readRank(x)] )
df = df.sort_values(['rank', "card1", "card2", "card3", "card4", "card5"], ascending = False)
print(df)
# value = readRank("QQQJA")
# print("this is value", dictRanking[value]) 


numbers = pd.to_numeric(df["Number"])
print(numbers)
rank = 0
sum = 0
for number in numbers:
    rank+=1
    sum = sum + rank*number
print("this is final answer: ", sum)
