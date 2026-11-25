from calculator import add, subtract, multiply, divide, CircleArea
def test_add():
    assert add(2, 3) == 5
def test_divide():
    assert divide(6, 2) == 3
def test_subtract():
    assert subtract(5,4) == 1
def test_multiply():
    assert multiply(2,5) == 10
def test_div_uneven():
    assert divide(5,2) == 2.5
def test_circleArea():
    assert CircleArea(-4) == "Error"