import pytest

from src.task_Barvynska import FormatFile

from tests.conftest import (convert_driver_to_file_dict, convert_driver_to_file_row, generate_random_driver)

d1 = generate_random_driver()
d2 = generate_random_driver()


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (
            convert_driver_to_file_row([d1], "abb"),
            convert_driver_to_file_dict([d1], "abb"),
        ),
        (
            convert_driver_to_file_row([d1, d2], "abb"),
            convert_driver_to_file_dict([d1, d2], "abb"),
        ),
    ],
)
def test_format_file_abbreviation_data(test_input, expected):
    assert FormatFile.format_file_abbreviation_data(test_input) == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (
            convert_driver_to_file_row([d1], "start"),
            convert_driver_to_file_dict([d1], "start"),
        ),
        (
            convert_driver_to_file_row([d1, d2], "end"),
            convert_driver_to_file_dict([d1, d2], "end"),
        ),
    ],
)
def test_format_file_time(test_input, expected):
    assert FormatFile.format_file_time(test_input) == expected
