import re

def day3_1():
    sum = 0
    board = list(open('2023/day3/input.txt'))
    chars = {(r, c): board[r][c] for r in range(len(board)-1) for c in range(len(board[0])-1)
                    if board[r][c] not in '01234566789.'}
    for r, row in enumerate(board):
        for number in re.finditer(r'\d+', row):
            edge = {(r, c) for r in (r-1, r, r+1)
                for c in range(number.start()-1, number.end()+1)}
            for o in edge & chars.keys():
                sum = sum + int(number.group())
    answer = sum
    return answer


print("The answer for part 1 is: ", day3_1())