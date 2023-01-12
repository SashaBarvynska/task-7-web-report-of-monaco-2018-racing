import pytest

from src.task_Barvynska import Drivers

from tests.conftest import generate_random_driver

test_driver = generate_random_driver()

d1 = generate_random_driver()
d2 = generate_random_driver()
d3 = generate_random_driver()

d4 = generate_random_driver("1:41.000")
d5 = generate_random_driver("1:46.000")
d6 = generate_random_driver("1:51.000")


def test_set_speed():
    speed = test_driver.speed
    test_driver.speed = 0
    test_driver.set_speed()
    assert test_driver.speed == speed


@pytest.mark.parametrize(
    "test_input_1, test_input_2, test_input_3, expected",
    [
        (
            {d1.abbreviation: {"driver": d1.driver, "car": d1.car}},
            {d1.abbreviation: d1.start_time},
            {d1.abbreviation: d1.end_time},
            [d1],
        ),
        (
            {
                d2.abbreviation: {"driver": d2.driver, "car": d2.car},
                d3.abbreviation: {"driver": d3.driver, "car": d3.car},
            },
            {d2.abbreviation: d2.start_time, d3.abbreviation: d3.start_time},
            {d2.abbreviation: d2.end_time, d3.abbreviation: d3.end_time},
            [d2, d3],
        ),
    ],
)
def test_build_report(test_input_1, test_input_2, test_input_3, expected):
    assert (
        Drivers.build_report(test_input_1, test_input_2, test_input_3).__repr__()
        == expected.__repr__()
    )


@pytest.mark.parametrize(
    "test_input_1, test_input_2, expected",
    [
        ([d4, d5], True, [d5, d4]),
        ([d4, d5, d6], False, [d4, d5, d6]),
    ],
)
def test_sort_data(test_input_1, test_input_2, expected):
    assert Drivers.sort_data(test_input_1, test_input_2) == expected


@pytest.mark.parametrize(
    "test_input_1, test_input_2, expected",
    [
        ([d1], d1.driver, [d1]),
        ([d1, d2, d3], d2.driver, [d2]),
        ([d1, d2, d3], d3.driver, [d3]),
    ],
)
def test_info_driver(test_input_1, test_input_2, expected):
    assert Drivers.info_driver(test_input_1, test_input_2) == expected
