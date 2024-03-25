from day2 import read_file, check_password, passwords_valid


def test_read_file():
    answer = read_file('2020/day2/input2.txt')
    first_answer = answer[0]
    first_answer['low'] = 3
    first_answer['high'] = 7
    first_answer['letter'] = 'r'
    first_answer['password'] = ' mxvlzcjrsqst'

def test_check_password():
    line = {
        "low": 1,
        "high":3,
        "letter": 'a',
        "password": 'abcdea'
    }
    assert check_password(line, True) == True

def test_passwords_valid():
    assert passwords_valid(True) == 422

def test_check_password_2():
    line = {
        "low": 1,
        "high":3,
        "letter": 'a',
        "password": 'abcdea'
    }
    assert check_password(line, False) == True

def test_passwords_valid_2():
    assert passwords_valid(False) == 451