import gudlft.server as server
from gudlft.server import app


class TestSummary:

    # def setup_method(self):
    #     self.client = app.test_client()
    #     server.data = DataLoader(
    #         club_file='test_clubs.json',
    #         competition_file='test_competitions.json'
    #     )

    def test_show_summary(self, mocker, client, mock_test_data):
        # mocker.patch.object(server, 'client', client)
        self.client = app.test_client()
        mocker.patch.object(server, 'data', mock_test_data)
        response = self.client.post(
            '/showSummary',
            data={'email': 'club@exemple.com'}
        )
        data = response.data.decode()
        data_list = [y for y in (x.strip() for x in data.splitlines()) if y]
        i1 = data_list.index('<h3>List of upcoming competitions:</h3>')
        i2 = data_list.index('Date: 2023-10-22 13:30:00</br>')
        i3 = data_list.index('Date: 2023-08-05 13:30:00</br>')
        i4 = data_list.index('<h3> List of past competitions:</h3>')
        i5 = data_list.index('Date: 2020-10-22 13:30:00</br>')
        i6 = data_list.index('Date: 2020-03-27 10:00:00</br>')
        assert i1 < i2 and i2 < i3 and i3 < i4 and i4 < i5 and i5 < i6

    def test_show_board(self, mocker,  mock_test_data):
        self.client = app.test_client()
        mocker.patch.object(server, 'data', mock_test_data)
        response = self.client.get(
            '/showPointsDisplayBoard'
        )
        data = response.data.decode()
        data_list = [y for y in (x.strip() for x in data.splitlines()) if y]
        try:
            i1 = data_list.index('club for test <br>')
        except ValueError:
            print(i1)
            assert False
        assert True
