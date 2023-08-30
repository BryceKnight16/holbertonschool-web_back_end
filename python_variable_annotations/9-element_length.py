#!/usr/bin/python3
"""
Module that gets the length of a list
and retuns a tuple of the list and the length
"""
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    function that  gets a list and returns a tuple of (str and int)
    """
    return[(i, len(i)) for i in lst]
