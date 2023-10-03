#!/usr/bin/python3
"""
Solving the lockboxes puzzle.
"""


def canUnlockAll(boxes):
    """
    Check if all boxes can be opened.
    """

    if not boxes or type(boxes) is not list:
        return False

    unlocked = [0]
    for n in unlocked:
        for key in boxes[n]:
            if key not in unlocked and key < len(boxes):
                unlocked.append(key)

    if len(unlocked) == len(boxes):
        return True
    return False
