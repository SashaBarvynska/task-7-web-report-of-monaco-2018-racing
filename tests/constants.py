from src.task_Barvynska.drivers import Driver

ABBR = [f"A{i}" for i in range(10, 99)]
DRIVER_NAMES = [f"Test{i}" for i in range(100)]
CARS = ["MERCEDES", "FERRARI", "AUDI"]
LIST_DRIVERS = [
    Driver(
        "DRR",
        "Daniel Ricciardo",
        "RED BULL RACING TAG HEUER",
        "12:14:12.054",
        "12:11:24.067",
        "57:12.013",
    ),
    Driver(
        "SVF", "Sebastian Vettel", "FERRARI", "12:02:58.917", "12:04:03.332", "1:04.415"
    ),
]
SORT_LIST_DRIVERS = [
    Driver(
        "SVF", "Sebastian Vettel", "FERRARI", "12:02:58.917", "12:04:03.332", "1:04.415"
    ),
    Driver(
        "DRR",
        "Daniel Ricciardo",
        "RED BULL RACING TAG HEUER",
        "12:14:12.054",
        "12:11:24.067",
        "57:12.013",
    ),
]
DICT_ABB = {
    "DRR": {"driver": "Daniel Ricciardo", "car": "RED BULL RACING TAG HEUER"},
    "SVF": {"driver": "Sebastian Vettel", "car": "FERRARI"},
}
DICT_TIME = {"SVF": "12:02:58.917", "DRR": "12:14:12.054"}
FILE_TIME = "SVF2018-05-24_12:02:58.917\nDRR2018-05-24_12:14:12.054\n\n"
FILE_END = "DRR2018-05-24_12:11:24.067\nSVF2018-05-24_12:04:03.332"
FILE_ABB = (
    "DRR_Daniel Ricciardo_RED BULL RACING TAG HEUER\nSVF_Sebastian Vettel_FERRARI\n"
)
