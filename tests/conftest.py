import pytest
from app import create_app
from app.models.pin import Pin
from app import db
from flask.signals import request_finished


@pytest.fixture
def app():
    # create the app with a test config dictionary
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    # close and remove the temporary database
    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


# This fixture gets called in every test that
# references "one_pin"
# This fixture creates a pin and saves it in the database
@pytest.fixture
def one_pin(app):
    new_pin = Pin(
        latitude=47.83, longitude=-122.33, description="Run around the park")
    db.session.add(new_pin)
    db.session.commit()


# This fixture gets called in every test that
# references "three_pins"
# This fixture creates pins and saves
# them in the database
@pytest.fixture
def three_pins(app):
    db.session.add_all([
        Pin(
            latitude=12.34, longitude=56.789, description="First random pin from conftest"),
        Pin(
            latitude=52.90, longitude=-100.99, description="Second random pin from conftest"),
        Pin(
            latitude=-23.8128, longitude=-16.2842, description="Third random pin from conftest")
    ])
    db.session.commit()
