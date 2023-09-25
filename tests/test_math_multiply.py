import pytest
products = [
    (2,3,6),
    (1,99,99),
    (0,99,0),
    (3,-4, -12),
    (-5, -5, 25),
    (2.5, 6.7,16.75)
]

@pytest.mark.parametrize('a, b, product',products) #decorator(special function that warps around other function) for test_multiply function 
def test_multiply( a, b, product): #inner function (test_multiply) is the test cases
    assert a*b == product