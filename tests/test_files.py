from unittest.mock import mock_open, patch
import pytest

from src.task_Barvynska import Files

from tests.constants import FILE_ABB, FILE_END, FILE_TIME


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("path_to_file_abbreviations.txt", FILE_ABB),
        ("path_to_file_start.log", FILE_TIME),
        ("path_to_file_end.log", FILE_END),
    ],
)
def test_open_file_success(test_input, expected):
    mock = mock_open(read_data=expected)
    with patch("builtins.open", mock):
        assert Files.open_files(test_input) == expected
        mock.assert_called_once_with(test_input, "r")


def test_find_all_files():
    with patch('os.walk') as mockwalk:
        mockwalk.return_value = [
            ("", (), ("start.log", "end.log", "abbreviations.txt")),
        ]
        assert Files.find_files("folder") == ['start.log', 'end.log', 'abbreviations.txt']


def test_find_any_files():
    with patch('os.walk') as mockwalk:
        mockwalk.return_value = [
            ("folder", (), ("end.log", "abbreviations.txt")),
        ]
        with pytest.raises(Exception) as error:
            Files.find_files("folder")
        assert str(error.value) == "Following files are missing: ['start.log']"
