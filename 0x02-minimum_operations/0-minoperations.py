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

    if not isinstance(n, int):
        return 0

    op = 0
    i = 2

    while (i <= n):
        if not (n % i):
            n = int(n / i)
            op += i
            i = 1
        i += 1

    return op
