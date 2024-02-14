def day2_1():
    with open('2023/day2/input.txt', encoding="utf-8") as file:

        game_id = 0
        sum_colors = 0
        valid = True

        for line in file:
            line = line.strip()
            game_id +=1
            line = line.split("; ")
            line[0] = line[0].split(": ")[1]
            for set_colors in line:
                blue, green, red = 0, 0, 0
                set_colors = set_colors.split(", ")
                for combination in set_colors:
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
                sum_colors = sum_colors + game_id
            valid = True
        return sum_colors

def day2_2():
    with open('2023/day2/input.txt', encoding="utf-8") as file:

        sum_colors = 0
        for line in file:
            blue, green, red = 0, 0, 0
            line = line.strip()
            line = line.split("; ")
            line[0] = line[0].split(": ")[1]
            for set_colors in line:
                set_colors = set_colors.split(", ")
                for combination in set_colors:
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
            sum_colors = sum_colors + red * green * blue
        return sum_colors

print("Answer of part 1 is: ", day2_1())
print("Answer of part 2 is: ", day2_2())
