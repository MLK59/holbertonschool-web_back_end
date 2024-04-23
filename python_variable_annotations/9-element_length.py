#!/user/bin/env python3
'''element length'''

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''return list of tuples, each containing an element and its length'''
    return [(i, len(i)) for i in lst]
