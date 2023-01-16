import os

import pytest

from src.app import get_app


@pytest.fixture()
def app():
    app = get_app()
    app.config.update({
        "TESTING": True,
    })
    os.environ["FOLDER_FILES"] = 'tests/test_data_files'
    yield app
    os.environ["FOLDER_FILES"] = ''


@pytest.fixture()
def client(app):
    return app.test_client()
