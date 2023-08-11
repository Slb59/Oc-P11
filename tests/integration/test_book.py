import gudlft.server as server
from http import HTTPStatus
from gudlft.server import app


def test_book_in_future(mocker, mock_test_data):
    client = app.test_client()
    mocker.patch.object(server, 'data', mock_test_data)
    response = client.get(
        '/book/Competition future/club for test'
        )
    assert response.status_code == HTTPStatus.OK
    data = response.data.decode()
    assert "<h2>Competition future</h2>" in data


def test_book_in_past(mocker, mock_test_data):
    client = app.test_client()
    mocker.patch.object(server, 'data', mock_test_data)
    response = client.get(
        '/book/Fall Classic/club for test'
        )
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_book_not_exists(mocker, mock_test_data):
    client = app.test_client()
    mocker.patch.object(server, 'data', mock_test_data)
    response = client.get(
        '/book/inconnu/club for test'
        )
    assert response.status_code == HTTPStatus.NOT_FOUND
