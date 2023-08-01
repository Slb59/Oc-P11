import pytest

# from gudlft.server import create_app


# @pytest.fixture
# def client():

#     # app = create_app({"TESTING": True})

#     with app.test_client() as client:
#         yield client


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
            "name": "Simply Lift",
            "email": "john@simplylift.co",
            "points": "13"
        },
        {
            "name": "Iron Temple",
            "email": "admin@irontemple.com",
            "points": "4"
        },
        {
            "name": "She Lifts",
            "email": "kate@shelifts.co.uk",
            "points": "12"
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
