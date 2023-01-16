import pytest
from task_Barvynska import Driver

from src.controller import get_driver
from tests.constants import LIST_DRIVERS


@pytest.mark.parametrize("drivers,key,value,expected", [
    (
        LIST_DRIVERS,
        "abbreviation",
        "DRR",
        Driver("DRR", "Daniel Ricciardo", "RED BULL RACING TAG HEUER", "12:14:12.054", "12:11:24.067", "57:12.013")
    ),
    (
        LIST_DRIVERS,
        "driver",
        "Sebastian Vettel",
        Driver("SVF", "Sebastian Vettel", "FERRARI", "12:02:58.917", "12:04:03.332", "1:04.415")
    ),
])
def test_get_driver(drivers, key, value, expected):
    assert get_driver(drivers, key, value) == expected
