import pytest

from gudlft.server import app


@pytest.fixture
def client():

    # app = create_app({"TESTING": True})

    with app.test_client() as client:
        yield client


@pytest.fixture
def clubtest():
    club1 = {
        "name": "Club to test",
        "email": "club@example.com",
        "points": "5"
    }
    return club1


@pytest.fixture
def test_clubs_data():
    return [
        {
            "name": "club for test",
            "email": "club@exemple.com",
            "points": "13"
        }
    ]


@pytest.fixture
def test_competitions_data():
    return [
        {
            "name": "Spring Festival",
            "date": "2020-03-27 10:00:00",
            "numberOfPlaces": "25"
        },
        {
            "name": "Fall Classic",
            "date": "2020-10-22 13:30:00",
            "numberOfPlaces": "13"
        }
    ]
