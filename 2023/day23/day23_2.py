from itertools import combinations

def read_input():
    with open('2023/day23/input.txt') as file:
        velocity = []
        coordinates = []
        for line in file:
            temp = line.strip()
            temp = temp.split(" @ ")
            temp_coordinates = [int(x) for x in temp[0].split("," )]
            temp_velocity = [int(x) for x in temp[1].split("," )]
            velocity.append(temp_velocity)
            coordinates.append(temp_coordinates)
    return coordinates, velocity

def line_intersection(line1, line2):
   xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
   ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

   def det(a, b):
       return a[0] * b[1] - a[1] * b[0]

   div = det(xdiff, ydiff)
   if div == 0:
      return 'lines do not intersect'

   d = (det(*line1), det(*line2))
   x = det(d, xdiff) / div
   y = det(d, ydiff) / div
   return x, y


def Main(begin, end):
    coordinates, velocity = read_input()

    sum = 0
    for i in combinations([*range(len(coordinates))], 2):

        x_1 = coordinates[i[0]][0] + velocity[i[0]][0]
        y_1 = coordinates[i[0]][1] + velocity[i[0]][1]
        x_2 = coordinates[i[1]][0] + velocity[i[1]][0]
        y_2 = coordinates[i[1]][1] + velocity[i[1]][1]
        line1 = [(coordinates[i[0]][0], coordinates[i[0]][1]), (x_1, y_1)]
        line2 = [(coordinates[i[1]][0], coordinates[i[1]][1]), (x_2, y_2)]
        answer = line_intersection(line1, line2)

        x_intersect = True
        y_intersect = True
        if answer != 'lines do not intersect' and  begin <= answer[0] <= end and begin <= answer[1]  <= end:
            if( velocity[i[0]][0] > 0 and answer[0] < coordinates[i[0]][0] or velocity[i[1]][0] > 0 and answer[0] < coordinates[i[1]][0]):
                x_intersect = False
            elif(velocity[i[0]][0] < 0 and answer[0] > coordinates[i[0]][0] or velocity[i[1]][0] < 0 and answer[0] > coordinates[i[1]][0]):
                x_intersect = False
            elif( velocity[i[0]][1] > 0 and answer[1] < coordinates[i[0]][1] or velocity[i[1]][1] > 0 and answer[1] < coordinates[i[1]][1]):
                y_intersect = False
            elif(velocity[i[0]][1] < 0 and answer[1] > coordinates[i[0]][1] or velocity[i[1]][1] < 0 and answer[1] > coordinates[i[1]][1]):
                y_intersect = False
            if x_intersect and y_intersect:
                sum+=1   
        print("")

    return sum

print("The final answer is", Main(200000000000000, 400000000000000))