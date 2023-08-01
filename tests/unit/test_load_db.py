from gudlft.db import loadClubs, loadCompetitions


class TestLoadDb:

    def test_loadClubs(clubs_data):
        assert loadClubs() == clubs_data

    def test_loadCompetitions(competitions_data):
        assert loadCompetitions() == competitions_data
