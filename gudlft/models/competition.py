class Competition:
    def __init__(self, name, date, numberOfPlaces=0):
        self.name = name
        self.date = date
        self.number_of_places = int(numberOfPlaces)

    def __str__(self) -> str:
        return f"<Competition - {self.name}>"

    def __eq__(self, __value: object) -> bool:
        return self.name == __value.name and self.date == __value.date
