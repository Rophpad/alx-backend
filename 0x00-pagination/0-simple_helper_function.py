#!/usr/bin/env python3
"""
Python function
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple containing  start index and an end index
    """
    end_idx = page * page_size
    return (end_idx - page_size, end_idx)
