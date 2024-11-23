import math

def test_should_return_square_root_of_positive_number():
    assert square_root(16) == 4
def test_should_raise_exception_for_negative_number():
    try:
        square_root(-9)
        assert False, "Test failed: square_root(-9) should raise ValueError."
    except ValueError as e:
        assert str(e) == "Cannot calculate the square root of a negative number.