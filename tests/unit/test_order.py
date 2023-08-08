from gudlft.db import Club, Competition, Order


class TestOrder:

    def test_init(self):
        new_competition = Competition(
            'premiere competition', "2023-08-07 16:30:00", 25
            )
        new_club = Club('nouveau club', 'club@example.com', 10)
        new_order = Order(new_club, new_competition, 10)
        print(new_order)
        assert str(new_order) == "[nouveau club - premiere competition : 10]"
