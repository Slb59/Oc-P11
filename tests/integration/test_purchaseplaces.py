import gudlft.server as server
import os

from http import HTTPStatus
from gudlft.server import app
from gudlft.db import DataLoader


class TestPurchasePlaces:

    # load the test database
    # data = DataLoader(
    #     club_file='test2_clubs.json',
    #     competition_file='test2_competitions.json'
    # )

    def setup_method(self):        
        self.client = app.test_client()
        os.environ['TESTING'] = 'True'
        # server.data = self.data

    def test_deduct_points_ok(self):
        # print(server.data)
        club_points_before = server.data.clubs[0].points
        competition_places_before =\
            server.data.competitions[0].number_of_places
        places_booked = 5

        result = self.client.post(
            "/purchasePlaces",
            data={
                "places": places_booked,
                "club": server.data.clubs[0].name,
                "competition": server.data.competitions[0].name
            }
        )
        # print(server.data)
        assert result.status_code == HTTPStatus.OK
        assert server.data.competitions[0].number_of_places == \
            competition_places_before - places_booked
        assert server.data.clubs[0].points == \
            club_points_before - places_booked
        assert server.data.clubs[0].points >= 0

    def test_not_enough_club_points(self):
        club_points_before = server.data.clubs[0].points
        competition_places_before =\
            server.data.competitions[0].number_of_places
        places_booked = club_points_before + 1
        result = self.client.post(
            "/purchasePlaces",
            data={
                "places": places_booked,
                "club": server.data.clubs[0].name,
                "competition": server.data.competitions[0].name
            }
        )
        assert result.status_code == HTTPStatus.OK
        assert server.data.competitions[0].number_of_places == \
            competition_places_before
        assert server.data.clubs[0].points == \
            club_points_before
        data = result.data.decode()
        assert "<li>Your club have not enough points</li>"\
            in data

    def test_competition_places_not_available(self):
        server.data.clubs[0].points = 100
        club_points_before = server.data.clubs[0].points
        competition_places_before =\
            server.data.competitions[0].number_of_places
        places_booked = competition_places_before + 1
        result = self.client.post(
            "/purchasePlaces",
            data={
                "places": places_booked,
                "club": server.data.clubs[0].name,
                "competition": server.data.competitions[0].name
            }
        )
        assert result.status_code == HTTPStatus.OK
        assert server.data.competitions[0].number_of_places == \
            competition_places_before
        assert server.data.clubs[0].points == \
            club_points_before
        data = result.data.decode()
        print(data)
        assert "<li>The competition have not enough places available</li>"\
            in data
