#!/usr/bin/env python3
"""
index_range: takes two arguments
            page - starting index
            page_size - size of the page
            Returns: a tuple of size two containing
            start index and end index corresponding the range of
            indexes to return in a list of those particular
            pagination parameters
"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns a tuple of size two containing start index
    and end index"""
    return (page_size * (page - 1), page_size * page)
