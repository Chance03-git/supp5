import math
def square_root(num):
    """Calculates the square root of a number.

    Args:
        number: The number to calculate the square root of.

    Returns:
        The square root of the number.

    Raises:
        ValueError: If the number is negative.
    """
    if num < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    return math.sqrt(num)


def test_should_return_square_root_of_positive_number():
    assert square_root(16) == 4
def test_should_raise_exception_for_negative_number():
    try:
        square_root(-9)
        assert False, "Test failed: square_root(-9) should raise ValueError."
    except ValueError as e:
        assert str(e) == "Cannot calculate the square root of a negative number."
def test_should_return_number_if_valid():
    """Tests that a valid number is returned if it is less than or equal to 4."""
    for _ in range(100):  # Run multiple tests to increase coverage
        try:
            result = process_random_number()
            assert result <= 4, f"Test failed: Returned number {result} is greater than 4."
        except ValueError as e:
            print(e)