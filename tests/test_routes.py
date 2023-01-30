from unittest.mock import patch

from flask import Response

from tests.constants import DRIVER_DRR, LIST_DRIVERS, LIST_DRIVERS_SORTED


@patch("src.routes.DriverAdaptor.sort_data", return_value=LIST_DRIVERS_SORTED)
def test_show_report_asc(mock_sort_data, client):
    response: Response = client.get("/report?order=asc")
    assert "FERRARI" in response.data.decode()
    assert response.status_code == 200
    mock_sort_data.assert_called_with(False)


@patch("src.routes.DriverAdaptor.sort_data", return_value=LIST_DRIVERS_SORTED)
def test_show_report_desc(mock_sort_data, client):
    response: Response = client.get("/report?order=desc")
    assert "FERRARI" in response.data.decode()
    assert response.status_code == 200
    mock_sort_data.assert_called_with(True)


@patch("src.routes", return_value=LIST_DRIVERS)
def test_show_drivers(mocker_get_drivers, client):
    response: Response = client.get("/report/drivers")
    assert "Romain Grosjean" in response.data.decode()
    assert response.status_code == 200


@patch("src.routes.DriverAdaptor.get_driver", return_value=DRIVER_DRR)
def test_get_info(mock_get_driver, client):
    response: Response = client.get("/report/drivers/DRR")
    assert "Daniel Ricciardo" in response.data.decode()
    assert response.status_code == 200
    mock_get_driver.assert_called_with("abbreviation", "DRR")
