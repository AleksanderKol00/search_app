import logging
from bisect import bisect_left
from turtledemo.penrose import inflatedart
from typing import Optional

from pydantic import BaseModel

from routes.static import ERROR_MSG

log = logging.getLogger(__name__)


class SearchItem(BaseModel):
    index: Optional[int]
    value: int
    message: Optional[str]


class SearchService:
    CONFORMATION_LEVEL = 0.1

    def __init__(self, data: list[int]) -> None:
        self.data = data

    def _get_index(self, value: int) -> Optional[int]:
        log.debug(f"Getting index for value: {value}")
        index = bisect_left(self.data, value)
        log.debug(f"bisect left index: {index}")

        # Check if there's value for given index
        if index != len(self.data) and self.data[index] == value:
            log.debug(f"Found value with exact index: {index}")
            return index

        log.debug(f"Didn't find value with exact index: {index}. Trying to find acceptable value")
        min_possible = value * (1 - self.CONFORMATION_LEVEL)
        max_possible_value = value * (1 + self.CONFORMATION_LEVEL)
        # Check left value
        if index > 0:
            if min_possible <= self.data[index - 1] <= max_possible_value:
                log.debug(
                    f"Left value matches the wanted value, index: {index - 1}, value: {self.data[index - 1]}")
                return index - 1

        # Check right value
        if index < len(self.data):
            if min_possible <= self.data[index] <= max_possible_value:
                log.debug(
                    f"Returned index matches the wanted value: {index},  index: {index}, value: {self.data[index]}")
                return index

        return None

    def find_item(self, value: int) -> SearchItem:
        index = self._get_index(value)
        msg = ERROR_MSG if index is None else ""
        value = self.data[index] if index is not None else value
        log.debug(f"Return search item with index: {index}, value: {value}, message: {msg}")
        return SearchItem(index=index, value=value, message=msg)
