import math
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Optional

from pandas import Timedelta


@dataclass
class Driver:
    abbreviation: str
    driver: str
    car: str
    start_time: str
    end_time: str
    speed: str = Optional[str]

    def _get_time_difference(self) -> timedelta:
        end = datetime.strptime(self.end_time, "%H:%M:%S.%f")
        start = datetime.strptime(self.start_time, "%H:%M:%S.%f")
        return end - start

    def set_speed(self) -> None:
        diff = self._get_time_difference()
        sec = Timedelta(diff).total_seconds()
        self.speed = self._convert_time(sec)

    @staticmethod
    def _convert_time(seconds) -> str:
        minutes = math.floor((seconds % 3600) / 60)
        seconds = seconds % 60
        return f"{minutes}:{seconds:06.3f}"

    def __repr__(self):
        return str(
            (
                self.abbreviation,
                self.driver,
                self.car,
                self.start_time,
                self.end_time,
                self.speed,
            )
        )


class Drivers:

    @classmethod
    def build_report(
        cls,
        content_abbreviations_file: dict[str: dict[str: str]],
        content_file_start: dict[str: dict[str: datetime]],
        content_file_end: dict[str: dict[str: datetime]],
    ) -> list[Driver]:
        drivers = []
        for abr, value in content_abbreviations_file.items():
            driver_object = Driver(
                abbreviation=abr,
                driver=value["driver"],
                car=value["car"],
                start_time=content_file_start[abr],
                end_time=content_file_end[abr],
            )
            driver_object.set_speed()
            drivers.append(driver_object)
        return drivers

    @staticmethod
    def sort_data(drivers: list[Driver], order: bool) -> list[Driver]:
        return sorted(drivers, key=lambda x: x.speed, reverse=order)

    @staticmethod
    def info_driver(drivers: list[Driver], driver: str) -> list[Driver]:
        return [driver_object for driver_object in drivers if driver_object.driver == driver]

    @staticmethod
    def print_report(sorted_list: list[Driver]) -> None:
        for index, value in enumerate(sorted_list):
            print(f"{index + 1}.{value.driver}     |{value.car}     |{value.speed}")
            if index == 14:
                print(
                    "_" * 66
                )
