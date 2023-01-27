from unittest.mock import patch

from flask import Response, render_template
from src.controller import DriverAdaptor
from tests.constants import DRIVER_DRR, LIST_DRIVERS, LIST_DRIVERS_SORTED


# @patch("src.routes.DriverAdaptor", return_value=LIST_DRIVERS)
# def test_show_report(mocker_DriverAdaptor, client):
#     response: Response = client.get("/report")
#     assert render_template('report.html', data=LIST_DRIVERS_SORTED).replace(" ", "") == response.data.decode().replace(" ", "")
#     assert response.status_code == 200
#     mocker_DriverAdaptor.assert_called_once()


# @patch("src.routes.get_drivers", return_value=LIST_DRIVERS)
# @patch("src.routes.Drivers.sort_data", return_value=LIST_DRIVERS_SORTED)
# def test_show_report_asc(mock_sort_data, mocker_get_drivers, client):
#     response: Response = client.get("/report?order=asc")
#     assert render_template('report.html', data=LIST_DRIVERS_SORTED).replace(" ", "") == response.data.decode().replace(" ", "")
#     assert response.status_code == 200
#     mock_sort_data.assert_called_with(LIST_DRIVERS, False)
#     mocker_get_drivers.assert_called_once()


# @patch("src.routes.get_drivers", return_value=LIST_DRIVERS)
# @patch("src.routes.Drivers.sort_data", return_value=LIST_DRIVERS)
# def test_show_report_desc(mock_sort_data, mocker_get_drivers, client):
#     response: Response = client.get("/report?order=desc")
#     assert render_template('report.html', data=LIST_DRIVERS).replace(" ", "") == response.data.decode().replace(" ", "")
#     assert response.status_code == 200
#     mock_sort_data.assert_called_with(LIST_DRIVERS, True)
#     mocker_get_drivers.assert_called_once()


# @patch("src.routes.get_drivers", return_value=LIST_DRIVERS)
# def test_show_drivers(mocker_get_drivers, client):
#     response: Response = client.get("/report/drivers")
#     assert render_template('drivers.html', data=LIST_DRIVERS).replace(" ", "") == response.data.decode().replace(" ", "")
#     assert response.status_code == 200
#     mocker_get_drivers.assert_called_once()


@patch("src.routes.DriverAdaptor", return_value=LIST_DRIVERS)
@patch("src.controller.DriverAdaptor.get_driver", return_value=DRIVER_DRR)
def test_get_info(mock_get_driver, mocker_get_drivers, client):
    response: Response = client.get("/report/drivers/DRR")
    assert render_template('driver_info.html', data=DRIVER_DRR).replace(" ", "") == response.data.decode().replace(" ", "")
    assert response.status_code == 200
    mock_get_driver.assert_called_with("abbreviation", "DRR")
    mocker_get_drivers.assert_called_once()
