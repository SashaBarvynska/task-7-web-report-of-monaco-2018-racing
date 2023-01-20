from task_Barvynska import Driver, Drivers, Files, FormatFile

from config import Config


def get_drivers() -> list[Driver]:
    file_start, file_end, abbreviations_file = Files.find_files(Config.FOLDER_FILES)
    list_drivers = Drivers.build_report(
        FormatFile.format_file_abbreviation_data(Files.open_files(abbreviations_file)),
        FormatFile.format_file_time(Files.open_files(file_start)),
        FormatFile.format_file_time(Files.open_files(file_end)),)
    return list_drivers


def get_driver(drivers: list[Driver], key: str, value) -> list[Driver]:
    return [driver_object for driver_object in drivers if getattr(driver_object, key) == value][0]
