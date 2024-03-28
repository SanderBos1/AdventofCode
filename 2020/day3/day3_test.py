from day3 import check_tree, read_file, check_length, part1_solution, part2_solution


def test_check_tree():
    matrix = read_file('2020/day3/input3.txt', 1)
    position = [3, 1]
    encountered = 0

    new_position, encountered = check_tree(position, encountered, matrix, 3, 1)

    assert new_position == [6, 2] and encountered == 1

def test_check_length():
    step = 3
    length, width = check_length(step)
    assert length == 323 and width == 32

def test_part1_solution():
    encountered = part1_solution()
    assert encountered == 176

def test_part2_solution():
    encountered = part2_solution()
    assert encountered == 5872458240

