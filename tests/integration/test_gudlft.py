import gudlft.server as server
from gudlft.server import app


class TestGudlft:

    client = app.test_client()
    competition = [
        {
            "name": "Test competition",
            "date": "2023-08-01 00:00:00",
            "numberOfPlaces": "10"
        }
    ]

    club = [
        {
            "name": "Test club",
            "email": "club@example.com",
            "points": "10"
        }
    ]

    def setup_method(self):
        server.competitions = self.competition
        server.clubs = self.club

    def test_deduct_points_ok(self):
        club_points_before = int(self.club[0]["points"])
        places_booked = 5

        result = self.client.post(
            "/purchasePlaces",
            data={
                "places": places_booked,
                "club": self.club[0]["name"],
                "competition": self.competition[0]["name"]
            }
        )

        assert result.status_code == 200
        assert int(self.club[0]["points"]) == club_points_before - places_booked