from bisect import bisect_left
from typing import Optional

from pydantic import BaseModel

from routes.static import ERROR_MSG


class SearchItem(BaseModel):
    index: Optional[int]
    value: int
    message: Optional[str]


class SearchService:
    def __init__(self, data: list[int]) -> None:
        self.data = data

    def _get_index(self, value: int) -> Optional[int]:
        index = bisect_left(self.data, value)
        if index != len(self.data) and self.data[index] == value:
            return index
        return None

    def find_item(self, value: int) -> SearchItem:
        index = self._get_index(value)
        msg = ERROR_MSG if index is None else ""

        return SearchItem(index=index, value=value, message=msg)
