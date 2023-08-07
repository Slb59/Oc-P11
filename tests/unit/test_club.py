import pytest
from gudlft.db import DataLoader, BookingException


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
        with pytest.raises(BookingException) as e_info:
            self.data.clubs[0].book(self.data.competitions[0], 10)
        assert "Your club have not enough points" in str(e_info.value)
        self.data.clubs[0].points = 20
        with pytest.raises(BookingException) as e_info:
            self.data.clubs[0].book(self.data.competitions[0], 17)
        assert "The competition have not enough places available" \
            in str(e_info.value)
