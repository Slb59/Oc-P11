import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

import gudlft.server as server
from gudlft.db import DataLoader


class TestStories:

    def setup_method(self):

        # load test data
        # server.data = DataLoader(
        #     club_file='test2_clubs.json',
        #     competition_file='test2_competitions.json'
        # )

        #start webdriver
        options = Options()
        options.use_chromium = True

        service = Service(
            executable_path="tests/fonctionnal_edge/msedgedriver.exe"
            )
        self.driver = webdriver.Edge(
            service=service,
            options=options,
            )
        self.driver.get("http://127.0.0.1:5000/")
        self.driver.minimize_window()
        self.driver.maximize_window()
        time.sleep(5)

    def teardown_method(self):
        self.driver.quit()

    def test_story1_login_scenario1(self):
        field_email = self.driver.find_element(By.ID, "email_field")
        field_email.send_keys("john@simplylift.co")
        time.sleep(2)
        field_email.submit()
        time.sleep(2)
        assert "Welcome, john@simplylift.co" in self.driver.page_source

    def test_story2_login_scanario2(self):
        field_email = self.driver.find_element(By.ID, "email_field")
        field_email.send_keys("unlonown@example.com")
        time.sleep(2)
        field_email.submit()
        time.sleep(2)
        assert "Cette adresse email n'est pas reconnue"\
            in self.driver.page_source
        
    def test_story3_logout(self):
        ...

