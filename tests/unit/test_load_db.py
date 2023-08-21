from freezegun import freeze_time
from gudlft.models.dataloader import DataLoader
from gudlft.models.competition import Competition
from gudlft.models.club import Club


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
        """Given: test_clubs.json and test_competitions.json
        files
        """
        self.data = DataLoader(
            club_file='test_clubs.json',
            competition_file='test_competitions.json'
            )

    def test_load_clubs(self, test_clubs_data):
        """
        When init instance, self.data.clubs
        has correct value
        """
        clubs = [
            Club(
                "club for test",
                "club@exemple.com",
                "13")
        ]
        assert self.data.clubs == clubs

    def test_load_competitions(self):
        """
        When init instance, self.data.competitions
        has correct value
        """
        competitions = [
            Competition(
                "Spring Festival",
                "2020-03-27 10:00:00",
                "25"),
            Competition(
                "Fall Classic",
                "2020-10-22 13:30:00",
                "13"),
            Competition(
                "Competition future",
                "2023-10-22 13:30:00",
                "13"),
            Competition(
                "Competition passee",
                "2023-08-05 13:30:00",
                "13")
        ]
        assert self.data.competitions == competitions

    @freeze_time("2023-08-01 00:00:00")
    def test_sort_competition(self):
        """
        When init instance, self.data.past_competitions 
        and future_compeitions has correct value
        """
        past_competitions = [
            Competition(
                "Fall Classic",
                "2020-10-22 13:30:00",
                "13"),
            Competition(
                "Spring Festival",
                "2020-03-27 10:00:00",
                "25")    
        ]
        future_competitions = [
            Competition(
                "Competition future",
                "2023-10-22 13:30:00",
                "13"),
            Competition(
                "Competition passee",
                "2023-08-05 13:30:00",
                "13")
        ]
        self.data = DataLoader(
            club_file='test_clubs.json',
            competition_file='test_competitions.json'
            )
        for c in self.data.past_competitions:
            print(c)
        print('---')
        for c in self.data.future_competitions:
            print(c)
        assert self.data.past_competitions == past_competitions
        assert self.data.future_competitions == future_competitions

    def test_print_data(self):
        """
        When init instance then I can print it
        """
        self.data = DataLoader(
            club_file='test_clubs.json',
            competition_file='test_competitions.json'
            )
        print(self.data)
        message = "\nClubs: \n"
        message += "- <Club - club for test>\n\n"
        message += "Competitions: \n"
        message += "- <Competition - Spring Festival>\n"
        message += "- <Competition - Fall Classic>\n"
        message += "- <Competition - Competition future>\n"
        message += "- <Competition - Competition passee>\n"
        print(message)
        assert str(self.data) == message
