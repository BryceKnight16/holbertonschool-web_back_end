#!/usr/bin/env python3
"""
Module that uses union to take a str and in/float and returns a tuple
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    function that takes a int/float and str and turns it into a tuple
    """
    return (k, v**2)
