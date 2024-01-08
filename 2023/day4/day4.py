def part1():
    with open("2023/day4/input.txt") as File:
        sum = 0
        for line in File:
            line = line.strip()
            line = line.split("| ")
            line[0] = line[0].split(": ")[1].strip()

            winning_numbers = [int(x) for x in line[0].split(" ") if x != ""]
            numbers_you_have = [int(x) for x in line[1].split(" ") if x != ""]

            points = 0

            first_seen = False
            for i in winning_numbers:
                if i in numbers_you_have:
                    if not first_seen:
                        points+=1
                        first_seen = True
                    else:
                        points = points *2
            sum = sum + points              
        return sum


def part2():

    with open("2023/day4/input.txt")  as fp:
        for count, line in enumerate(fp):
            pass

    ticket_amounts = {}
    for i in range(count+1):
        key = i+1
        ticket_amounts[key] = 1

    current = 0
    with open("2023/day4/input.txt") as File:
        #for i in range(len(File))
        for line in File:
            current +=1
            line = line.strip()
            line = line.split("| ")
            line[0] = line[0].split(": ")[1].strip()

            winning_numbers = [int(x) for x in line[0].split(" ") if x != ""]
            numbers_you_have = [int(x) for x in line[1].split(" ") if x != ""]
            repeats = ticket_amounts[current]
            
            tickets_won = 0
            for i in winning_numbers:
                if i in numbers_you_have:
                    tickets_won+=1
            
            start = current+tickets_won
            while(start > current):
                ticket_amounts[start] +=1*repeats
                start-=1
            
        answer = 0
        for value in ticket_amounts.values():
            answer = answer + value

        return answer



print("The answer of part 1 is: ", part1())
print("The answer of part 2 is: ", part2())