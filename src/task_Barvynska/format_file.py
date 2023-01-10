from datetime import datetime


class FormatFile:

    @staticmethod
    def format_file_abbreviation_data(
        content: str,
    ) -> dict[str: dict[str: str]]:
        line_objects = {}
        for line in content.strip().split("\n"):
            line_words = line.split("_")
            line_objects.update(
                {line_words[0]: {"driver": line_words[1], "car": line_words[2]}}
            )
        return line_objects

    @staticmethod
    def format_file_time(
        content: str,
    ) -> dict[str: dict[str: datetime]]:
        line_objects = {}
        for line in content.split():
            line_objects.update({line[0:3]: line[14:]})
        return line_objects
