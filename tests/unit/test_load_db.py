from gudlft.db import DataLoader


class TestLoadDb:

    data = DataLoader(
        club_file='test_clubs.json',
        competition_file='test_competitions.json'
        )

    def test_loadClubs(self, test_clubs_data):
        assert self.data.clubs == test_clubs_data

    def test_loadCompetitions(self, test_competitions_data):
        assert self.data.competitions == test_competitions_data
