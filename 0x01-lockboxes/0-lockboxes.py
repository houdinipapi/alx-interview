#!/usr/bin/python3


def canUnlockAll(boxes):
    """
    Check if all boxes can be opened using BFS.
    Args:
        boxes (List[List[int]]): List of lists representing boxes and keys.
    Returns:
        bool: True if all boxes can be opened, else False.
    """

    if not boxes:
        return False

    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    stack = [0]

    while stack:
        current_box = stack.pop()
        keys = boxes[current_box]

        for key in keys:
            if 0 <= key < n and not visited[key]:
                visited[key] = True
                stack.append(key)

        return all(visited)
