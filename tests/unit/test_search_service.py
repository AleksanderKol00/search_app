import pytest

from services.search_service import SearchService


@pytest.mark.parametrize("data, value, exp_index", [
    ([0, 10, 20, 100], 100, 3),
    ([], 100, None),
    ([1100, 1200], 1150, 0)
])
def test_get_index(data, value, exp_index):
    assert exp_index == SearchService(data).find_item(value).index
