import pytest

from gudlft.server import app
from gudlft.db import Club, Competition


@pytest.fixture
def client():

    # app = create_app({"TESTING": True})

    with app.test_client() as client:
        yield client


@pytest.fixture
def clubtest():
    club_dict = {
        "name": "Club to test",
        "email": "club@example.com",
        "points": "5"
    }
    return Club(**club_dict)


@pytest.fixture
def test_clubs_data():
    club_dict = {
            "name": "club for test",
            "email": "club@exemple.com",
            "points": "13"
        }
    return [Club(**club_dict)]


@pytest.fixture
def test_competitions_data():
    competition1_dict = {
            "name": "Spring Festival",
            "date": "2020-03-27 10:00:00",
            "numberOfPlaces": "25"
        }
    competition2_dict = {
            "name": "Fall Classic",
            "date": "2020-10-22 13:30:00",
            "numberOfPlaces": "13"
        }
    return [ 
        Competition(**competition1_dict),
        Competition(**competition2_dict)
    ]
