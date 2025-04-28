#!/usr/bin/python3
"""
This module defines the canUnlockAll function,
which determines if all boxes can be opened.
The function takes a list of boxes, where each box contains a list of keys
to other boxes.
The function returns True if all boxes can be opened, otherwise False.
The function uses a set to keep track of opened boxes and
a list to manage keys.
"""


def canUnlockAll(boxes):
    opened_boxes = set([0])
    keys = boxes[0][:]
    while keys:
        key = keys.pop()

        if key < len(boxes) and key not in opened_boxes:
            opened_boxes.add(key)
            keys.extend(boxes[key])

    return len(opened_boxes) == len(boxes)
