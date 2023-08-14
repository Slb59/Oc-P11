class Order:
    def __init__(self, club, competition, nb_of_places):
        self.club = club
        self.competition = competition
        self.nb_of_places = int(nb_of_places)

    def __str__(self) -> str:
        order_string = f'[{self.club.name} - {self.competition.name} '
        order_string += f': {self.nb_of_places}]'
        return order_string
