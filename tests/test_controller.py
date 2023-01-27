from unittest.mock import patch

import pytest

from src.controller import DriverAdaptor
from tests.constants import (DICT_ABB, DICT_TIME, DRIVER_DRR, DRIVER_SVF,
                             LIST_DRIVERS)


@pytest.mark.parametrize("key,value,expected", [
    (
        "abbreviation",
        "DRR",
        DRIVER_DRR
    ),
    (
        "driver",
        "Sebastian Vettel",
        DRIVER_SVF
    ),
])
def test_get_driver(key, value, expected):
    instance = DriverAdaptor()
    assert instance.get_driver(key, value) == expected


@patch(
    "task_Barvynska.files.Files.find_files",
    return_value=["path_1", "path_2", "path_3"],
)
@patch(
    "task_Barvynska.files.Files.open_files",
    return_value="file_content",
)
@patch(
    "task_Barvynska.format_file.FormatFile.format_file_abbreviation_data",
    return_value=DICT_ABB,
)
@patch(
    "task_Barvynska.format_file.FormatFile.format_file_time",
    return_value=DICT_TIME,
)
@patch("task_Barvynska.drivers.Drivers.build_report", return_value=LIST_DRIVERS)
def test_get_drivers(mock_build_report, mock_format_file_time, mock_format_file_abbreviation_data, mock_open_files, mock_find_files):
    instance = DriverAdaptor()
    assert instance.list_drivers == LIST_DRIVERS
    mock_build_report.assert_called_with(DICT_ABB, DICT_TIME, DICT_TIME)
    mock_format_file_time.assert_called_with("file_content")
    mock_format_file_abbreviation_data.assert_called_with("file_content")
    mock_open_files.assert_called_with("path_2")
    mock_find_files.assert_called_with("data_files")
