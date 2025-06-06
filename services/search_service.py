from bisect import bisect_left
from typing import Optional

from pydantic import BaseModel, validate_email

from routes.static import ERROR_MSG


class SearchItem(BaseModel):
    index: Optional[int]
    value: int
    message: Optional[str]


class SearchService:
    CONFORMATION_LEVEL = 0.1

    def __init__(self, data: list[int]) -> None:
        self.data = data

    def _get_index(self, value: int) -> Optional[int]:
        index = bisect_left(self.data, value)

        # Check if there's value for given index
        if index != len(self.data) and self.data[index] == value:
            return index

        min_possible = value * (1 - self.CONFORMATION_LEVEL)
        max_possible_value = value * (1 + self.CONFORMATION_LEVEL)
        # Check left value
        if index > 0:
            if min_possible <= self.data[index - 1] <= max_possible_value:
                return index - 1

        # Check right value
        if index < len(self.data):
            if min_possible <= self.data[index] <= max_possible_value:
                return index

        return None

    def find_item(self, value: int) -> SearchItem:
        index = self._get_index(value)
        msg = ERROR_MSG if index is None else ""

        return SearchItem(index=index, value=value, message=msg)
