import gudlft.server as server

from http import HTTPStatus
from gudlft.server import app
from gudlft.models.dataloader import DataLoader


class TestLoginLogout:

    # load the test database
    data = DataLoader(
        club_file='test_clubs.json',
        competition_file='test_competitions.json'
    )

    def setup_method(self):
        self.client = app.test_client()
        server.data = self.data

    def test_home_should_status_code_ok(self):
        response = self.client.get('/')
        assert response.status_code == HTTPStatus.OK

    def test_home_should_return_correcthtml(self):
        response = self.client.get('/')
        data = response.data.decode()
        assert "title>GUDLFT Registration</title>" in data
        assert "<form action=\"showSummary\" method=\"post\">" in data

    def test_post_login_OK(self):
        first_email_in_db = server.data.clubs[0].email
        # print(first_email_in_db)
        response = self.client.post(
            '/showSummary',
            data={'email': first_email_in_db}
        )
        assert response.status_code == HTTPStatus.OK
        assert first_email_in_db in response.get_data(as_text=True)

    def test_post_login_KO(self):
        # mocker.patch.object(server, 'data', self.data)
        response = self.client.post(
            '/showSummary',
            data={'email': 'unknown@exemple.com'}
        )
        assert response.status_code == HTTPStatus.OK
        data = response.data.decode()
        assert "<li>!!! Cette adresse email n&#39;est pas reconnue</li>"\
            in data

    def test_logout(self):

        result = self.client.get("/logout")
        assert result.status_code == 302
