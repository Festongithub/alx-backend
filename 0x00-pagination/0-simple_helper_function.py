#!/usr/bin/env python3
"""simple helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ return a tuple of size two containing a start index and an
    end index corresponding to the range of indexes to return in
    list for those particular pagination parameters
    """
    return ((page - 1) * page_size, page_size * page)
