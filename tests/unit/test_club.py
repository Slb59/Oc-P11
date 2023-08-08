import pytest
from gudlft.db import (
    NotEnoughtPointsError, NotEnoughtPlacesError,
    MaxPlacesPerCompetitionError,
    DataLoader, Club, Competition, Order
)


class TestClub:

    def setup_method(self):
        self.data = DataLoader(
            club_file='test_clubs.json',
            competition_file='test_competitions.json'
        )

    def test_book(self):
        self.data.clubs[0].book(self.data.competitions[0], 10)
        assert self.data.clubs[0].points == 3
        assert self.data.competitions[0].number_of_places == 15
        with pytest.raises(Exception) as e_info:
            self.data.clubs[0].book(self.data.competitions[0], 10)
        assert e_info.type is NotEnoughtPointsError
        self.data.clubs[0].points = 20
        self.data.competitions[0].number_of_places = 5
        with pytest.raises(Exception) as e_info:
            self.data.clubs[0].book(self.data.competitions[0], 12)
        assert e_info.type is NotEnoughtPlacesError
        self.data.competitions[0].number_of_places = 20
        with pytest.raises(Exception) as e_info:
            self.data.clubs[0].book(self.data.competitions[0], 15)
        assert e_info.type is MaxPlacesPerCompetitionError

    def test_init(self):
        new_club = Club('nouveau club', 'club@example.com', 10)
        assert str(new_club) == '<Club - nouveau club>'

    def test_already_booked(self):
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
