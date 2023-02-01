from unittest.mock import patch

import pytest
from flask import Response

from tests.constants import ASC_SVF, DESC_SVF, DRIVER_DRR, DRR


@pytest.mark.parametrize("order, sort", [
    (
        "desc", DESC_SVF
    ),
    (
        "asc", ASC_SVF
    ),
    ])
def test_show_report(order, sort, client):
    response: Response = client.get(f"/report?order={order}")
    assert sort in response.data.decode()
    assert response.status_code == 200


def test_show_drivers(client):
    response: Response = client.get("/report/drivers")
    assert DRR in response.data.decode()
    assert response.status_code == 200


@patch("src.routes.DriverAdaptor.get_driver", return_value=DRIVER_DRR)
def test_get_info(mock_get_driver, client):
    response: Response = client.get("/report/drivers/DRR")
    assert "Daniel Ricciardo" in response.data.decode()
    assert response.status_code == 200
    mock_get_driver.assert_called_with("abbreviation", "DRR")
