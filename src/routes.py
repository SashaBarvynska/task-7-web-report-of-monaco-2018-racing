from flask import render_template, request
from task_Barvynska import Drivers

from src.app import app
from src.controller import get_driver, get_drivers


@app.route('/', methods=['GET'])
@app.route('/report', methods=['GET'])
def show_report():
    list_drivers = get_drivers()
    list_driver_sorted = Drivers.sort_data(list_drivers, request.args.get('order') == "desc")
    return render_template('report.html', data=list_driver_sorted)


@app.route('/report/drivers', methods=['GET'])
def show_drivers():
    list_drivers = get_drivers()
    return render_template('drivers.html', data=list_drivers)


@app.route('/report/drivers/<driver_code>', methods=['GET'])
def get_info(driver_code):
    list_drivers = get_drivers()
    driver = get_driver(list_drivers, 'abbreviation', driver_code)
    return render_template('driver_info.html', data=driver)
