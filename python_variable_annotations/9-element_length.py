#!/usr/bin/env python3
"""
Module that gets the length of a list
and retuns a tuple of the list and the length
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    function that  gets a list and returns a tuple of (str and int)
    """
    return[(i, len(i)) for i in lst]
