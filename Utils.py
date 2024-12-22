def remove_lowest_values(numbers, count=5):
    """
    Removes the 'count' lowest values from the given list of numbers.

    Args:
        numbers (list): The list of numbers to process.
        count (int): The number of lowest values to remove (default is 5).

    Returns:
        list: The updated list with the lowest values removed.
    """
    for _ in range(count):
        if numbers:  # Ensure the list is not empty
            min_value = min(numbers)  # Find the smallest value
            numbers.remove(min_value)  # Remove the first occurrence of the minimum value

    return numbers


def truncate_float(number, decimals):
    """
    Truncate a float to the specified number of decimal places.

    Parameters:
    - number (float): The float number to truncate.
    - decimals (int): The number of decimal places to retain.

    Returns:
    - float: The truncated float.
    """
    if decimals < 0:
        raise ValueError("The number of decimals must be non-negative.")
    factor = 10 ** decimals
    return int(number * factor) / factor