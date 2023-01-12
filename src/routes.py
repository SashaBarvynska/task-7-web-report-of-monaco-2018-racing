from flask import render_template, request

from src.app import app
from src.controller import get_drivers, get_driver
from src.task_Barvynska import Drivers


@app.route('/report', methods=['GET'])
def show_report():
    list_drivers = get_drivers()
    list_driver_sorted = Drivers.sort_data(list_drivers, request.args.get('order') == "desc")
    return render_template('report.html', data=list_driver_sorted)


@app.route('/report/drivers', methods=['GET'])
def show_drivers():
    abbr = request.args.get('driver_id')
    list_drivers = get_drivers()
    if abbr:
        driver = get_driver(abbr)
        return render_template('driver_info.html', data=driver)
    return render_template('drivers.html', data=list_drivers)
