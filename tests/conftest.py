
import pytest

from main import app as flask_app


@pytest.fixture(scope="module")
def app():
    flask_app.config.update({
        "TESTING": True,
    })
    yield flask_app


@pytest.fixture(scope="module")
def client(app):
    return app.test_client()
