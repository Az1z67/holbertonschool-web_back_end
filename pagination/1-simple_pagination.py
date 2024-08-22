#!/usr/bin/env python3
"""Pagination"""


from typing import Tuple, List
import csv
import math


index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names"""
    
    DATA_FILE = "Popular_Baby_Names.csv"
    
    def __init__(self):
        self.__dataset = None
    
    def dataset(self) -> List:
        if self.__dataset is None:
            with open(self.DATA_FILE, 'r') as f:
                reader = csv.reader(f)
                self.__dataset = [row for row in reader]
        return self.__dataset
    
    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        
        start, end = index_range(page, page_size)
        return self.dataset()[start:end]
    
def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """perform pagination"""
    return ((page - 1) * page_size, page * page_size)
