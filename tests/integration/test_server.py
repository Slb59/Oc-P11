from http import HTTPStatus
from gudlft.server import create_app


def test_home_should_status_code_ok(client):
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK


def test_home_should_return_correcthtml(client):
    response = client.get('/')
    data = response.data.decode()
    assert "title>GUDLFT Registration</title>" in data
    assert "<form action=\"showSummary\" method=\"post\">" in data


def test_post_login_OK(client, clubtest):
    mocker.patch.object(create_app, 'clubs', clubtest)
    response = client.post(
        '/showSummary',
        data={'email': clubtest['email']}
    )
    assert response.status_code == HTTPStatus.OK
    assert 'club@gmail.com' in response.get_data(as_text=True)
