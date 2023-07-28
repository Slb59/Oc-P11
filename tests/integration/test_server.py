from http import HTTPStatus


def test_home_should_status_code_ok(client):
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK


# def test_should_return_hello_world(client):
#     response = client.get('/')
#     data = response.data.decode()  # Permet de décoder la data dans la requête
#     assert data == 'Hello, World!'
