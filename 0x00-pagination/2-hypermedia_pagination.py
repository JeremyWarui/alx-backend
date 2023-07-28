#!/usr/bin/env python3
"""
Implement a get_hyper method: that takes the same arguments (and defaults)
            as get_page and returns a dictionary containing the
            following key-value pairs:
            1. page_size: the length of the returned dataset page
            2. page: the current page number
            3. data: the dataset page (equivalent to return from
            previous task)
            4. next_page: number of the next page, None if no next page
            5. prev_page: number of the previous page, None if no
            previous page
            6. total_pages: the total number of pages in the dataset
            as an integer
"""

import csv
import math
from typing import List

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """returns page of the dataset"""
        assert all(isinstance(arg, int) and arg > 0
                   for arg in (page, page_size))
        indices = index_range(page, page_size)
        start = indices[0]
        end = indices[1]

        try:
            return self.dataset()[start: end]
        except IndexError:
            return []

    def get_hyper(self,  page: int = 1, page_size: int = 10) -> dict:
        """returns a dictionary containing the
            following key-value pairs:
            1. page_size: the length of the returned dataset page
            2. page: the current page number
            3. data: the dataset page (equivalent to return from previous task)
            4. next_page: number of the next page, None if no next page
            5. prev_page: number of the previous page, None if no previous page
            6. total_pages: the total number of pages in the dataset as an
            integer
        """
        page_content = self.get_page(page, page_size)
        total_data = len(self.dataset())
        total_pages = math.ceil(total_data / page_size)

        return {
            "page_size": page_size,
            "page": page,
            "data": page_content,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page != 1 else None,
            "total_pages": total_pages
        }
