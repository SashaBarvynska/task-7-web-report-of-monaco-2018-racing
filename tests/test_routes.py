from flask import Response, render_template

from src.controller import get_driver
from tests.constants import LIST_DRIVERS, LIST_DRIVERS_SORTED


def test_show_report(client):
    response: Response = client.get("/report")
    assert render_template('report.html', data=LIST_DRIVERS_SORTED).replace(" ", "") == response.data.decode().replace(" ", "")
    assert response.status_code == 200


def test_show_report_asc(client):
    response: Response = client.get("/report?order=asc")
    assert render_template('report.html', data=LIST_DRIVERS_SORTED).replace(" ", "") == response.data.decode().replace(" ", "")
    assert response.status_code == 200


def test_show_report_desc(client):
    response: Response = client.get("/report?order=desc")
    assert render_template('report.html', data=LIST_DRIVERS).replace(" ", "") == response.data.decode().replace(" ", "")
    assert response.status_code == 200


def test_show_drivers(client):
    response: Response = client.get("/report/drivers")
    assert render_template('drivers.html', data=LIST_DRIVERS).replace(" ", "") == response.data.decode().replace(" ", "")
    assert response.status_code == 200


def test_get_info(client):
    response: Response = client.get("/report/drivers/DRR")
    driver = get_driver(LIST_DRIVERS, 'abbreviation', "DRR")
    assert render_template('driver_info.html', data=driver).replace(" ", "") == response.data.decode().replace(" ", "")
    assert response.status_code == 200
