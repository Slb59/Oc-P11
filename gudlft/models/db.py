# import os


class NotEnoughtPointsError(Exception):
    def __init__(self, points, message="Your club doesn't have enough points"):
        self.points = points
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message


class NotEnoughtPlacesError(Exception):
    def __init__(
            self, places,
            message="The competition doesn't have enough places available"
            ):
        self.places = places
        self.message = message
        super().__init__(self.message)


class MaxPlacesPerCompetitionError(Exception):
    def __init__(
            self, maxvalue,
            message="Max places per competition reached"
            ):
        self.maxvalue = maxvalue
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        return 'You cannot purchase more than '\
            + str(self.maxvalue) + ' places for a competition'


class Club:

    MAX_BOOK_PLACES_PER_COMPETITION = 12

    def __init__(self, name, email, points):
        self.name = name
        self.email = email
        self.points = int(points)
        self.orders = []

    def __str__(self) -> str:
        return f"<Club - {self.name}>"

    def __eq__(self, __value: object) -> bool:
        return self.name == __value.name

    def already_booked(self, competition) -> int:
        """ give the number of places already booked for a competition """
        total = 0
        for order in self.orders:
            if order.competition == competition:
                total += order.nb_of_places
        return total

    def book(self, competition, nb_of_places) -> None:
        """
        book a nb_of_places for a competion :
        decrease the points of the club and the places
        avalaible for a competition and save the order information
        :param competition: must be a competition instance
        :param nb_of_places: number of places to book
        :raise NotEnoughtPointsError: if club doesn't have enought points
        :raise NotEnoughtPlacesError: if competition places available
        are < nb_of_places
        :raise MaxPlacesPerCompetitionError if nb_of_places > 12
        (MAX_BOOK_PLACES_PER_COMPETITION)
        """
        match nb_of_places:
            case _ as value if value > self.points:
                raise NotEnoughtPointsError(self.points)
            case _ as value if value > competition.number_of_places:
                raise NotEnoughtPlacesError(competition.number_of_places)
            case _ as value if self.already_booked(competition) + value\
                    > self.MAX_BOOK_PLACES_PER_COMPETITION:
                raise MaxPlacesPerCompetitionError(
                    self.MAX_BOOK_PLACES_PER_COMPETITION)
            case _ as value:
                competition.number_of_places -= nb_of_places
                self.points -= nb_of_places
                self.orders.append(Order(self, competition, nb_of_places))

    # def book_old(self, competition, nb_of_places):
    #     if nb_of_places > self.points:
    #         raise NotEnoughtPointsError(self.points)
        
    #     elif nb_of_places > competition.number_of_places:
    #         raise NotEnoughtPlacesError(competition.number_of_places)
        
    #     elif self.already_booked(competition) + nb_of_places\
    #             > self.MAX_BOOK_PLACES_PER_COMPETITION:
    #         raise MaxPlacesPerCompetitionError(
    #             self.MAX_BOOK_PLACES_PER_COMPETITION)
        
    #     else:
    #         competition.number_of_places -= nb_of_places
    #         self.points -= nb_of_places
    #         self.orders.append(Order(self, competition, nb_of_places))


class Competition:
    def __init__(self, name, date, numberOfPlaces=0):
        self.name = name
        self.date = date
        self.number_of_places = int(numberOfPlaces)

    def __str__(self) -> str:
        return f"<Competition - {self.name}>"

    def __eq__(self, __value: object) -> bool:
        return self.name == __value.name and self.date == __value.date


class Order:
    def __init__(self, club: Club, competition: Competition, nb_of_places):
        self.club = club
        self.competition = competition
        self.nb_of_places = int(nb_of_places)

    def __str__(self) -> str:
        order_string = f'[{self.club.name} - {self.competition.name} '
        order_string += f': {self.nb_of_places}]'
        return order_string
    