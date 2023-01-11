from flask import Flask, render_template, request

from src.task_Barvynska import Drivers, Files, FormatFile

app = Flask(__name__)


@app.route('/report', methods=['GET'])
def show_report():
    list_drivers = get_drivers()
    list_driver_sorted = Drivers.sort_data(list_drivers, request.args.get('order') == "desc")
    return render_template('report.html', data=list_driver_sorted, len=len(list_driver_sorted))


@app.route('/report/drivers', methods=['GET'])
def show_drivers():
    abbr = request.args.get('driver_id')
    list_drivers = get_drivers()
    if abbr:
        driver = list(filter(lambda x: x.abbreviation == abbr, list_drivers))[0]
        return render_template('driver_info.html', data=driver)
    return render_template('drivers.html', data=list_drivers, len=len(list_drivers))


def get_drivers():
    file_start, file_end, abbreviations_file = Files.find_files('D:\\Sasha\\Projects\\task-7-web-report-of-monaco-2018-racing\\data_files')
    list_drivers = Drivers.build_report(
        FormatFile.format_file_abbreviation_data(Files.open_files(abbreviations_file)),
        FormatFile.format_file_time(Files.open_files(file_start)),
        FormatFile.format_file_time(Files.open_files(file_end)),)
    return list_drivers


if __name__ == '__main__':
    app.run(debug=True)
