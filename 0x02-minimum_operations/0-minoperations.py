#!/usr/bin/python3
""" Script that computes a minimum operations
    needed in a CopyAll.
"""


def minOperations(n):
    """
    Method for compute the minimum number
    of operations

    Args:
        n: input val
        factor_list: List to save
    Return: the sum of the operations
    """
    if n < 2:
        return 0
    factor_list = []
    i = 1
    while n != 1:
        i += 1
        if n % i == 0:
            while n % i == 0:
                n /= i
                factor_list.append(i)
    return sum(factor_list)
