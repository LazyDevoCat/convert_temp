# -*- encoding: utf-8 -*-
"""
This file contains supporting logic

1. is_float (Check if the user's input convertible to float type)
"""
from typing import Any


def is_float(arg: Any) -> bool:
    """
    Check if the user's input convertible to float type
    """
    try:
        float(arg)
        return True
    except ValueError:
        return False
