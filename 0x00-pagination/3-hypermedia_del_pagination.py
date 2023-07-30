#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
Implement a get_hyper_index method with two integer arguments:
        index with a None default value and page_size with default value of 10
    The method should return a dictionary with the following key-value pairs:
    index: the current start index of the return page. That is the index
        of the first item in the current page. For example if requesting
        page 3 with page_size 20, and no data was removed from the dataset,
        the current index should be 60.
    next_index: the next index to query with. That should be the index
                of the first item after the last item on the current page.
    page_size: the current page size
    data: the actual page of the dataset
"""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> dict:
        """return a dictionary with the following key-value pairs:
        index: the current start index of the return page.
                That is the index of the first item in the current page.
                For example if requesting page 3 with page_size 20, and
                no data was removed from the dataset,the current index
                should be 60.
        next_index: the next index to query with. That should be the index
                of the first item after the last item on the current page.
        page_size: the current page size
        data: the actual page of the dataset
        """
        assert 0 <= index < len(self.dataset())
        indexed_data = self.indexed_dataset()
        indexed_page = {}

        for i in range(len(self.dataset())):
            if len(indexed_page) >= page_size:
                break
            if i in indexed_data:
                indexed_page[i] = indexed_data[i]
        page = list(indexed_page.values())
        page_index = indexed_page.keys()
        return {
            "index": index,
            "next_index": max(page_index) + 1,
            "page_size": len(page),
            "data": page
        }
