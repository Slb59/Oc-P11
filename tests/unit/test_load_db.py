from gudlft.db import DataLoader


class TestLoadDb:
    """
    Given : 2 file test_clubs.json and test_competitions.json
    in the json path
    When : DataLoader is call
    Then : return a data object with club and competion attribut
    club and competition attribut are dictionnary tha contains
    the json data
    """

    def setup_method(self):
        self.data = DataLoader(
            club_file='test_clubs.json',
            competition_file='test_competitions.json'
            )

    def test_loadClubs(self, test_clubs_data):
        assert self.data.clubs == test_clubs_data

    def test_loadCompetitions(self, test_competitions_data):
        assert self.data.competitions == test_competitions_data
