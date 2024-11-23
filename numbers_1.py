import math
import random
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
def process_random_number():
    """Picks a random integer between 1 and 100 and processes it based on conditions.

    Returns:
        The processed number if no exception is raised.

    Raises:
        ValueError: If the processed number is greater than 4.
    """
    number = random.randint(1, 100)
    print(f"Random number picked: {number}")  # Debugging statement

    if number % 2 == 0:
        pass  # Do nothing if even
    else:
        number *= 2  # Multiply by 2 if odd

    if number % 3 == 0:
        number //= 3  # Divide by 3 if divisible by 3

    if number % 4 == 0:
        number *= 4  # Multiply by 4 if divisible by 4

    if number > 4:
        raise ValueError(f"Number {number} is greater than 4.")

    return number
def find_divisibles(n):
    """Finds integers between 1 and 10 that are divisible by the given integer.

    Args:
        n: The integer to check divisibility against.

    Returns:
        A list of integers between 1 and 10 that are divisible by n.

    Raises:
        ValueError: If n is 0 to prevent division by zero.
    """
    if n == 0:
        raise ValueError("Division by zero is not allowed.")
    
    return [i for i in range(1, 11) if i % n == 0]

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
def test_should_raise_exception_for_number_greater_than_4():
    """Tests that an exception is raised if the processed number is greater than 4."""
    try:
        while True:  # Keep running until a ValueError is raised
            process_random_number()
    except ValueError as e:
        assert "is greater than 4" in str(e), "Test failed: Exception message incorrect."
def test_should_return_divisibles_for_positive_number():
    """Tests the find_divisibles function with a positive integer."""
    assert find_divisibles(2) == [2, 4, 6, 8, 10], "Test failed: find_divisibles(2) should return [2, 4, 6, 8, 10]."
    assert find_divisibles(3) == [3, 6, 9], "Test failed: find_divisibles(3) should return [3, 6, 9]."