#!/usr/bin/python3
"""Module for determining if all boxes can be opened."""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list): A list of lists representing boxes and their keys.

    Returns:
        bool: True if all boxes can be opened, else False.
    """
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = boxes[0]

    for key in keys:
        if 0 <= key < n and not unlocked[key]:
            unlocked[key] = True
            keys.extend(boxes[key])

    return all(unlocked)


if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))
