import json
import os

from distutils.util import strtobool
from datetime import datetime
from .club import Club
from .competition import Competition


class DataLoader:
    """ Load the clubs and competitions data """
    def __init__(self,
                 data_path='gudlft/json/',
                 club_file='clubs.json',
                 competition_file='competitions.json'
                 ):
        self.data_path = data_path
        self.club_file = club_file
        self.competition_file = competition_file

        if self.club_file is not None and self.competition_file is not None:
            # load clubs
            self.clubs = self._loadClubs()
            self.clubs.sort(key=lambda x: x.name)
            self.current_club = None

            # load competitions
            self.competitions = self._loadCompetitions()
            self.past_competitions, self.future_competitions\
                = self._sort_competitions()
            self.past_competitions.sort(
                key=lambda x: x.date, reverse=True)
            self.future_competitions.sort(
                key=lambda x: x.date, reverse=True)

    def _loadClubs(self) -> list:
        """ Load club json file
        and return a liste of Club instances
        """
        filename = self.data_path + self.club_file

        with open(filename) as c:
            listOfClubs = json.load(c)['clubs']
            clubs = [Club(**club) for club in listOfClubs]
            return clubs

    def _sort_competitions(self):
        """
        dispatch self.competitions in past_competition and
        futur competition
        """

        # change datetime for functionnal testing
        TESTING = strtobool(os.getenv('TESTING'))
        current_date = datetime.now()
        if TESTING:
            current_date = "2023-08-01 00:00:00"
            current_date = datetime.strptime(current_date, "%Y-%m-%d %H:%M:%S")

        competitions_in_past = []
        competition_in_future = []
        for competition in self.competitions:
            date_competition = datetime.strptime(
                competition.date, '%Y-%m-%d %H:%M:%S'
                )
            if date_competition < current_date:
                competitions_in_past.append(competition)
            else:
                competition_in_future.append(competition)
        return competitions_in_past, competition_in_future

    def _loadCompetitions(self):
        """ Load competiton json file
        and return a liste of Competition instances
        """

        filename = self.data_path + self.competition_file

        with open(filename) as comps:
            listOfCompetitions = json.load(comps)['competitions']
            competitions = [Competition(**comp) for comp in listOfCompetitions]
            return competitions

    def __str__(self):
        """ Print list of clubs
        and list of competitions
        """
        message = "\nClubs: \n"
        for club in self.clubs:
            message += f"- {club}\n"
        message += "\nCompetitions: \n"
        for comp in self.competitions:
            message += f"- {comp}\n"
        return message
