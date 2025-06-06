from unittest.mock import patch, mock_open

from services.load_data_service import get_data_from_file


def test_get_data_from_file():
    file_data = "0\n100\n200\n300\n"
    expected_data = [0, 100, 200, 300]

    with patch("builtins.open", mock_open(read_data=file_data)):
        data = get_data_from_file("")

    assert data == expected_data
