#!/usr/bin/python3

"""
Minimum Operations
"""


def minOperations(n):
    """
    Calculate the minimum number of operations needed
    to obtain 'n' H characters in the file.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The minimum number of operations.

    If 'n' is impossible to achieve, return 0.

    The two available operations are 'Copy All' and 'Paste'.
    This function finds the fewest number of operations by
    calculating the prime factors of 'n'
    and summing them up, representing the minimum number of operations needed.
    """

    # If 'n' is less than or equal to 1, it's impossible
    # to achieve 'n' H characters.
    if n <= 1:
        return n

    factors = []
    i = 2

    # Calculate the prime factors of 'n' and store them in the
    # 'fators' list.
    while i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1

    # Return the sum of the factors, representing the minimum
    # number of operations required.
    return sum(factors)
