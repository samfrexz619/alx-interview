#!/usr/bin/python3
"""
validUTF8
"""


def validUTF8(data):
    """
    Bit manipulationbthat determines if a given data
    set represents a valid UTF-8 encoding
    Args:
        data: data will be rep by a list
              of int
    Return: True or False
    """

    n_bytes = 0

    m1 = 1 << 7
    m2 = 1 << 6

    for x in data:
        m = 1 << 7
        if n_bytes == 0:
            while m & i:
                n_bytes += 1
                m = m >> 1
            if n_bytes == 0:
                continue
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            if not (x & m1 and not (x & m2)):
                return False
        n_bytes -= 1
    return n_bytes == 0
