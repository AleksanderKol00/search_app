import pytest
from starlette.testclient import TestClient

from main import app
from routes.static import ERROR_MSG
from schemas.search import SearchItemResponse


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def test_mock_init_data():
    app.state.data = [0, 10, 20, 100]


@pytest.mark.parametrize("value, expected_response", [
    pytest.param(100, SearchItemResponse(index=3, value=100, message=""), id="index found"),
    pytest.param(400, SearchItemResponse(index=None, value=400, message=ERROR_MSG), id="index not found")
])
def test_search(value, expected_response, test_mock_init_data, client):
    response = client.get(f"/search/{value}/")

    assert response.status_code == 200
    assert response.json()["index"] == expected_response.index
    assert response.json()["value"] == expected_response.value
    assert response.json()["message"] == expected_response.message
