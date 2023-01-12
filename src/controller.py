from src.task_Barvynska import Drivers, Files, FormatFile


def get_drivers():
    file_start, file_end, abbreviations_file = Files.find_files('..\\data_files')
    list_drivers = Drivers.build_report(
        FormatFile.format_file_abbreviation_data(Files.open_files(abbreviations_file)),
        FormatFile.format_file_time(Files.open_files(file_start)),
        FormatFile.format_file_time(Files.open_files(file_end)),)
    return list_drivers


def get_driver(abbr):
    return list(filter(lambda x: x.abbreviation == abbr, get_drivers()))[0]
