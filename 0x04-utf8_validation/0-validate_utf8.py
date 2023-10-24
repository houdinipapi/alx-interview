#!/usr/bin/python3

"""
Determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Validate if a list of integers represents a valid UTF-8 encoding.

    Args:
        data (list of int): A list of integers representing bytes.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    # Initialize a variable to keep track of the
    # number of bytes in the current character.
    num_bytes = 0

    for byte in data:
        # Check the most significant bit (leftmost bit) of the current byte.
        # If it's 0, it's a single-byte character or a continuation byte.
        if num_bytes == 0:
            if (byte >> 7) == 0:
                num_bytes = 0
            elif (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            else:
                return False
        else:
            # Check if the current byte is a
            # continuation byte (starts with 10).
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    # If there are leftover bytes to complete a character, it's not valid.
    return num_bytes == 0
