import json


def loadClubs():

    filename = 'gudlft/json/clubs.json'

    with open(filename) as c:
        listOfClubs = json.load(c)['clubs']
        return listOfClubs


def loadCompetitions():

    filename = 'gudlft/json/competitions.json'

    with open(filename) as comps:
        listOfCompetitions = json.load(comps)['competitions']
        return listOfCompetitions
