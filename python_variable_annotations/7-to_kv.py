#!/user/bin/env python
""" complex types string and int/float to tuple """

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return tuple of string and float"""
    return (k, v ** 2)
