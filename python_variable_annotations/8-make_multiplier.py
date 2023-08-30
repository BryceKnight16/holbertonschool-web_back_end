#!/usr/bin/env python3
"""
Module using callable to use two functions that work together
and multpile the variable mutliplier to the do multiple function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    function that takes a float multipler as an arg and returns
    a function that multiplies a float by the multiplier
    """
    def do_multiple(a: float) -> float:
        """
        function that does the multiplying
        """
        return a * multiplier

    return do_multiple
