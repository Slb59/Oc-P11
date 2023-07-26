from locust import HttpUser, task


class GudlftPerfTest(HttpUser):
    @task(6)
    def home(self):
        self.client.get("/")
