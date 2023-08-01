from gudlft.db import DataLoader


class TestLoadDb:

    data = DataLoader(
        club_file='test_clubs.json',
        competition_file='test_competitions.json'
        )

    def test_loadClubs(test_clubs_data):
        assert data.clubs == test_clubs_data

    def test_loadCompetitions(test_competitions_data):
        assert data.competitions == test_competitions_data
