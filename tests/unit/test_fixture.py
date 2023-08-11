import datetime
from freezegun import freeze_time


def test_club_fixture(clubtest):
    assert clubtest.email == "club@example.com"


@freeze_time("2012-01-14")
def test():
    assert datetime.datetime.now() == datetime.datetime(2012, 1, 14)
