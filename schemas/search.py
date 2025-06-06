from typing import Optional

from pydantic import BaseModel


class SearchItemResponse(BaseModel):
    index: Optional[int]
    value: int
    message: Optional[str]
