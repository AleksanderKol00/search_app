import pytest

from services.search_service import SearchService


@pytest.mark.parametrize("data, value, exp_index", [
    ([0, 10, 20, 100], 100, 3),
    ([], 100, None)
])
def test_get_index(data, value, exp_index):
    assert exp_index == SearchService(data).get_index(value)
