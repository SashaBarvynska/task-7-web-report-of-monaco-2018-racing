import os
import pathlib


class Files:
    @staticmethod
    def open_files(file: str) -> str:
        with open(file, "r") as reader:
            return reader.read()

    @staticmethod
    def find_files(path_to_folder: str) -> list[str, str, str]:
        files_name = ["start.log", "end.log", "abbreviations.txt"]
        pathes = []

        [
            [pathes.append(os.path.join(root, i)) for i in files_name if i in files]
            for root, _, files in os.walk(path_to_folder)
        ]

        files_in_folder = list(map(lambda x: pathlib.Path(x).name, pathes))
        missing_files = list(filter(lambda x: x not in files_in_folder, files_name))
        if missing_files:
            raise FileNotFoundError(f"Following files are missing: {missing_files}")
        return pathes
