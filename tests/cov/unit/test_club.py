import pytest

from gudlft.models.dataloader import DataLoader
from gudlft.models.competition import Competition
from gudlft.models.club import (
    NotEnoughtPointsError, NotEnoughtPlacesError,
    MaxPlacesPerCompetitionError,
    Club
)
from gudlft.models.order import Order


class TestClub:
    """
    Given : data from test_clubs.json and test_competitions.json
    files
    Then test the club instance behaviour
    """

    def setup_method(self):
        """
        Load data from json files
        first club is 13 points, first competition is 25 places
        """
        self.data = DataLoader(
            club_file='test_clubs.json',
            competition_file='test_competitions.json'
        )

    def test_book_not_enought_points(self):
        """
        When: I book 15 places
        Then: a NotEnoughtPointsError exception is raised
        """
        with pytest.raises(Exception) as e_info:
            self.data.clubs[0].book(self.data.competitions[0], 15)
        assert e_info.type is NotEnoughtPointsError

    def test_book_not_enought_places(self):
        """
        Given: I set 20 points to the club and 5 places to the competition
        When: I book 12 places
        Then: a NotEnoughtPlacesError exception is raised
        """
        self.data.clubs[0].points = 20
        self.data.competitions[0].number_of_places = 5
        with pytest.raises(Exception) as e_info:
            self.data.clubs[0].book(self.data.competitions[0], 12)
        assert e_info.type is NotEnoughtPlacesError

    def test_max_places_reached(self):
        """
        When: I book 10 places and then 3 places
        Then: a MaxPlacesPerCompetitionError exception is raised
        """
        self.data.competitions[0].number_of_places = 20
        self.data.clubs[0].book(self.data.competitions[0], 10)
        with pytest.raises(Exception) as e_info:
            self.data.clubs[0].book(self.data.competitions[0], 3)
        assert e_info.type is MaxPlacesPerCompetitionError

    def test_book_ok(self):
        """
        When: I book 10 places
        Then: clubs points and competition places are decreases
        """
        self.data.clubs[0].book(self.data.competitions[0], 10)
        assert self.data.clubs[0].points == 3
        assert self.data.competitions[0].number_of_places == 15

    def test_init(self):
        """
        When: I create a new club instance
        Then: I can print it
        """
        new_club = Club('nouveau club', 'club@example.com', 10)
        print(Club.__doc__)
        assert str(new_club) == '<Club - nouveau club>'

    def test_already_booked(self):
        """
        When: I order several places
        Then: the already_booked function is incremented
        """

        new_club = Club('nouveau club', 'club@example.com', 10)
        new_competition1 = Competition(
            'premiere competition', "2023-08-07 16:30:00", 25
            )
        new_competition2 = Competition(
            'deuxieme competition', "2023-08-07 17:30:00", 25
            )
        new_club.orders.append(Order(new_club, new_competition1, 10))
        new_club.orders.append(Order(new_club, new_competition1, 5))
        new_club.orders.append(Order(new_club, new_competition2, 20))
        assert new_club.already_booked(new_competition1) == 15
        assert new_club.already_booked(new_competition2) == 20
