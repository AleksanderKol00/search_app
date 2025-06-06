from fastapi import APIRouter, Request

from schemas.search import SearchItemResponse
from services.search_service import SearchService

router = APIRouter()


@router.get("/{value}/", response_model=SearchItemResponse)
def search(value: int, request: Request):
    search_service = SearchService(request.app.state.data)
    item = search_service.find_item(value)
    return SearchItemResponse(index=item.index, value=item.value, message=item.message)
