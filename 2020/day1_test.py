from day1 import summation, summation_2, read_file

def test_loading():
    for i in read_file('2020/input1.txt'):
        assert type(i) == int
        
def test_summation():
    assert summation() == 514579
    
def test_summation_2():
    assert summation_2() == 241861950