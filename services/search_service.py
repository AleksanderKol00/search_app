from bisect import bisect_left
from typing import Optional


class SearchService:
    def __init__(self, data: list[int]) -> None:
        self.data = data

    def get_index(self, value: int) -> Optional[int]:
        index = bisect_left(self.data, value)
        if index != len(self.data) and self.data[index] == value:
            return index
        return None
