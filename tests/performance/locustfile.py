from locust import HttpUser, task


class GudlftPerfTest(HttpUser):

    @task
    def home(self):
        """ test home route """
        self.client.get("/")

    @task
    def showSummary(self):
        """ test summary page with post email """
        self.client.get("/showSummary")
        self.client.post("/showSummary", data={"email": "club@exemple.com"})

    @task
    def book(self):
        """ test book route """
        self.client.get("/book/Test competition3/club for test")

    @task
    def purchasePlaces(self):
        """ test purchase one place """
        self.client.post(
            "/purchasePlaces",
            data={
                "competition": "Test competition3",
                "club": "club for test",
                "places": 1
                }
            )

    @task
    def clubs_display(self):
        """ test board route """
        self.client.get('/showPointsDisplayBoard')

    @task
    def logout(self):
        """ test logout route """
        self.client.get('/logout')
