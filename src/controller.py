import os

from task_Barvynska import Driver, Drivers, Files, FormatFile


def get_drivers():
    file_start, file_end, abbreviations_file = Files.find_files(os.environ.get('FOLDER_FILES') or '..\\data_files')
    list_drivers = Drivers.build_report(
        FormatFile.format_file_abbreviation_data(Files.open_files(abbreviations_file)),
        FormatFile.format_file_time(Files.open_files(file_start)),
        FormatFile.format_file_time(Files.open_files(file_end)),)
    return list_drivers


def get_driver(drivers: list[Driver], key: str, value):
    return [driver_object for driver_object in drivers if driver_object.__dict__[key] == value][0]
