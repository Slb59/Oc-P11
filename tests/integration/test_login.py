import gudlft.server as server

from http import HTTPStatus
from gudlft.server import app


class TestLoginLogout:

    client = app.test_client()

    def test_home_should_status_code_ok(self):
        response = self.client.get('/')
        assert response.status_code == HTTPStatus.OK

    def test_home_should_return_correcthtml(self):
        response = self.client.get('/')
        data = response.data.decode()
        assert "title>GUDLFT Registration</title>" in data
        assert "<form action=\"showSummary\" method=\"post\">" in data

    def test_post_login_OK(self, clubtest):
        # mocker.patch('gudlft.db.loadClubs', return_value=clubtest)
        # print(db.loadClubs())
        # print(clubtest['email'])
        first_email_in_db = server.clubs[0]["email"]
        response = self.client.post(
            '/showSummary',
            data={'email': first_email_in_db}
        )
        assert response.status_code == HTTPStatus.OK
        data = response.data.decode()
        print(data)
        assert first_email_in_db in response.get_data(as_text=True)

    def test_post_login_KO(self):

        response = self.client.post(
            '/showSummary',
            data={'email': 'unknown@exemple.com'}
        )
        assert response.status_code == HTTPStatus.OK
        data = response.data.decode()
        assert "<li>!!! Cette adresse email n&#39;est pas reconnue</li>"\
            in data
