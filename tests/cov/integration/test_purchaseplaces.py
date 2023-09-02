import html
import gudlft.server as server

from http import HTTPStatus
from gudlft.server import app
from gudlft.models.dataloader import DataLoader


class TestPurchasePlaces:

    # load the test database
    data = DataLoader(
        club_file='test2_clubs.json',
        competition_file='test2_competitions.json'
    )

    def setup_method(self):
        self.client = app.test_client()
        server.data = self.data

    def test_deduct_points_ok(self):
        """
        Given : I want 5 places booked
        When : I call /purchasePlaces route
        Then : The number of points and places are decreased
        """

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

        assert result.status_code == HTTPStatus.OK
        assert server.data.competitions[0].number_of_places == \
            competition_places_before - places_booked
        assert server.data.clubs[0].points == \
            club_points_before - places_booked
        assert server.data.clubs[0].points >= 0

    def test_not_enough_club_points(self):
        """
        Given: I want to purchase more than points club avalaible
        When: I call purchasePlaces route
        Then: a corresponding message is printed in the html
        """
        server.data.clubs[0].points = 10
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
        # print(html.unescape(data))
        assert "<li>Your club doesn't have enough points</li>"\
            in html.unescape(data)

    def test_competition_places_not_available(self):
        """
        Given: I want to purchase more than places competition avalaible
        When: I call purchasePlaces route
        Then: a corresponding message is printed in the html
        """
        server.data.clubs[0].points = 100
        server.data.competitions[0].number_of_places = 10
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
        assert "The competition doesn't have enough places available"\
            in html.unescape(data)

    def test_purchase_more_than_12_places(self):
        """
        Given: I want to purchase more than max places for a competition
        When: I call purchasePlaces route
        Then: a corresponding message is printed in the html
        """
        server.data.clubs[0].points = 100
        # server.data.competitions[0].number_of_places = 25
        places_booked = 15
        result = self.client.post(
            "/purchasePlaces",
            data={
                "places": places_booked,
                "club": server.data.clubs[0].name,
                "competition": server.data.competitions[1].name
            }
        )
        data = result.data.decode()
        assert "You cannot purchase more than 12 places for a competition"\
            in data
