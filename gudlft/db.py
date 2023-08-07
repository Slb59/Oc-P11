# import os
import json


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
            self.clubs = self._loadClubs()
            self.competitions = self._loadCompetitions()

    def _loadClubs(self):

        filename = self.data_path + self.club_file

        with open(filename) as c:
            listOfClubs = json.load(c)['clubs']
            clubs = [Club(**club) for club in listOfClubs]
            return clubs

    def _loadCompetitions(self):

        filename = self.data_path + self.competition_file

        with open(filename) as comps:
            listOfCompetitions = json.load(comps)['competitions']
            competitions = [Competition(**comp) for comp in listOfCompetitions]
            return competitions

    def __str__(self):
        message = "\nClubs: \n"
        for club in self.clubs:
            message += f"- {club}\n"
        message += "\nCompetitions: \n"
        for comp in self.competitions:
            message += f"- {comp}\n"
        return message


class BookingException(Exception):
    pass


class Club:
    def __init__(self, name, email, points):
        self.name = name
        self.email = email
        self.points = int(points)

    def __str__(self) -> str:
        return f"<Club - {self.name}>"

    def __eq__(self, __value: object) -> bool:
        return self.name == __value.name

    def book(self, competition, nb_of_places):
        if nb_of_places > self.points:
            raise BookingException('Your club have not enough points')
        if nb_of_places > competition.number_of_places:
            raise BookingException(
                'The competition have not enough places available'
                )
        else:
            competition.number_of_places -= nb_of_places
            self.points -= nb_of_places


class Competition:
    def __init__(self, name, date, numberOfPlaces=0):
        self.name = name
        self.date = date
        self.number_of_places = int(numberOfPlaces)

    def __str__(self) -> str:
        return f"<Competition - {self.name}>"

    def __eq__(self, __value: object) -> bool:
        return self.name == __value.name and self.date == __value.date
