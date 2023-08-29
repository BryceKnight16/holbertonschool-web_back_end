#!/usr/bin/env python3
"""
Module that takes a list containing integers and
floats as input and returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    a function that returns the mixed list
    """
    return sum(mxd_lst)
