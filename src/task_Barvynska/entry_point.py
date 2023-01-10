from argparse import ArgumentParser, Namespace

from .drivers import Drivers
from .files import Files
from .format_file import FormatFile


def init_args() -> Namespace:
    parser = ArgumentParser(description="Add driver")
    parser.add_argument("--files", required=True)
    parser.add_argument("--asc", action="store_false")
    parser.add_argument("--desc", action="store_true")
    parser.add_argument("--driver")
    args = parser.parse_args()
    return args


def main() -> None:
    args = init_args()
    if not args.files:
        raise Exception("Required argument not specified '--files'")
    file_start, file_end, abbreviations_file = Files.find_files(args.files)
    list_drivers = Drivers.build_report(
        FormatFile.format_file_abbreviation_data(
            Files.open_files(abbreviations_file)
        ),
        FormatFile.format_file_time(Files.open_files(file_start)),
        FormatFile.format_file_time(Files.open_files(file_end)),
    )
    if args.driver:
        Drivers.print_report(Drivers.info_driver(list_drivers, args.driver))
    else:
        order = bool(args.desc)
        print("********************order: ", order)
        Drivers.print_report(Drivers.sort_data(list_drivers, order))
