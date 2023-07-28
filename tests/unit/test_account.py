# import pytest


def test_club_fixture(clubtest):
    assert clubtest['email'] == "club@gmail.com"
