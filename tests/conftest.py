import random
from datetime import datetime, timedelta

from src.task_Barvynska.drivers import Driver

from tests.constants import ABBR, CARS, DRIVER_NAMES


def generate_random_driver(speed=None) -> Driver:
    driver = f'{random.choice(DRIVER_NAMES)} - {random.randint(1, 100)}'
    car = random.choice(CARS)
    abbr = random.choice(ABBR)
    now = datetime.now()
    time_now = str(now)[11:-3]
    end_time = now + timedelta(seconds=random.randint(0, 120))
    time_end = str(end_time)[11:-3]
    driver = Driver(abbr, driver, car, time_now, time_end)
    if speed:
        driver.speed = speed
    else:
        driver.set_speed()
    return driver


def convert_driver_to_file_row(drivers: list[Driver], file: str) -> str:
    if file == "abb":
        return "\n".join(
            [
                f"{driver.abbreviation}_{driver.driver}_{driver.car}"
                for driver in drivers
            ]
        )
    elif file == "start":
        return "\n".join(
            [
                f"{driver.abbreviation}2018-05-24_{driver.start_time}"
                for driver in drivers
            ]
        )
    elif file == "end":
        return "\n".join(
            [f"{driver.abbreviation}2018-05-24_{driver.end_time}" for driver in drivers]
        )
    else:
        return ""


def convert_driver_to_file_dict(drivers: list[Driver], file: str) -> dict:
    drivers_dict = {}
    for driver in drivers:
        if file == "abb":
            drivers_dict.update(
                {driver.abbreviation: {"driver": driver.driver, "car": driver.car}}
            )
        elif file == "start":
            drivers_dict.update({driver.abbreviation: driver.start_time})
        elif file == "end":
            drivers_dict.update({driver.abbreviation: driver.end_time})
    return drivers_dict
