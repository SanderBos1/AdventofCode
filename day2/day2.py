def day2_1():
    with open('day2/input.txt') as file:

        game_id = 0
        sum = 0
        valid = True

        for line in file:
            line = line.strip()
            game_id +=1
            line = line.split("; ")
            line[0] = line[0].split(": ")[1]
            for set in line:
                blue, green, red = 0, 0, 0
                set = set.split(", ")
                for combination in set:
                    combination = combination.split(" ")
                    if combination[1] == "blue":
                        blue = blue + int(combination[0])
                    elif combination[1] == "green":
                        green = green + int(combination[0])          
                    elif combination[1] == "red":
                        red = red + int(combination[0])
                if red > 12 or green > 13 or blue > 14:
                    valid = False
                    break
            if valid:
                sum = sum + game_id             
            valid = True
        return sum
    

def day2_2():
    with open('day2/input.txt') as file:

        sum = 0
        for line in file:
            blue, green, red = 0, 0, 0
            line = line.strip()
            line = line.split("; ")
            line[0] = line[0].split(": ")[1]
            for set in line:
                set = set.split(", ")
                for combination in set:
                    combination = combination.split(" ")
                    number = int(combination[0])
                    if combination[1] == "blue":
                        if number > blue:
                            blue = number
                    elif combination[1] == "green":
                        if number > green:
                            green = number      
                    elif combination[1] == "red":
                        if number > red:
                            red = number 
            sum = sum + red * green * blue        
        return sum


print("Answer of part 1 is: ", day2_1())
print("Answer of part 2 is: ", day2_2())
