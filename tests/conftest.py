import pytest

# from datetime import datetime

from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service

from freezegun import freeze_time

from gudlft.server import app
from gudlft.models.dataloader import DataLoader
from gudlft.models.competition import Competition
from gudlft.models.club import Club

# from flask import jsonify


@pytest.fixture
def client():
    # app = create_app({"TESTING": True})
    with app.test_client() as client:
        yield client


@pytest.fixture
def driver_edge_init(request):
    options = Options()
    options.use_chromium = True
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # options.add_argument('--headless')
    service = Service(
        executable_path="tests/fonctionnal/msedgedriver.exe"
        )
    edge_driver = webdriver.Edge(
        service=service,
        options=options,
        )
    request.cls.driver = edge_driver

    edge_driver.get("http://127.0.0.1:5000/")
    edge_driver.minimize_window()
    edge_driver.maximize_window()

    yield

    edge_driver.quit()


@pytest.fixture
@freeze_time("2023-08-01 00:00:00")
def mock_test_data():
    return DataLoader(
            club_file='test_clubs.json',
            competition_file='test_competitions.json'
        )


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


# @pytest.fixture
# def mock_load_data():
#     data = DataLoader(
#         club_file='test2_clubs.json',
#         competition_file='test2_competitions.json'
#     )
