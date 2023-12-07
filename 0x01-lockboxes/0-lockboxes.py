#!/usr/bin/python3

"""
Problem: You have n number of locked boxes in front of you.
         Each box is numbered sequentially from 0 to n - 1
         and each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """
    Function that checks with boolean value the list type and
    length
    """
    if type(boxes) is not list:
        return False
    elif (len(boxes)) == 0:
        return False
    for j in range(1, len(boxes) - 1):
        boxes_checked = False
        for idx in range(len(boxes)):
            boxes_checked = j in boxes[idx] and j != idx
            if boxes_checked:
                break
        if boxes_checked is False:
            return boxes_checked
    return True
