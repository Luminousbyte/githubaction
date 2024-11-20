from src.math_operations import additionition, subtractiontraction

def test_addition():
    assert addition(2,3)==5
    assert addition(-1,1)==0
    
def test_subtraction():
    assert subtraction(5,3)==2
    assert subtraction(4,3)==1
    assert subtraction(3,3)==0
    assert subtraction(2,3)==-1