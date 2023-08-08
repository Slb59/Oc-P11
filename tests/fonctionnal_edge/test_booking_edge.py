import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

# import gudlft.server as server
# from gudlft.db import DataLoader


class TestStories:

    def setup_method(self):

        # load test data
        # server.data = DataLoader(
        #     club_file='test2_clubs.json',
        #     competition_file='test2_competitions.json'
        # )

        # start webdriver
        options = Options()
        options.use_chromium = True
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument('--headless')
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
        time.sleep(3)

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

    def test_story3_logout_from_summary(self):
        self.test_story1_login_scenario1()
        field_logout = self.driver.find_element(By.CLASS_NAME, "logout_link")
        field_logout.click()
        assert self.driver.current_url == 'http://127.0.0.1:5000/'

    def test_story3_logout_from_book(self):
        self.test_story1_login_scenario1()
        field_book = self.driver.find_element(By.CLASS_NAME, "book_link")
        field_book.click()
        field_logout = self.driver.find_element(By.CLASS_NAME, "logout_link")
        field_logout.click()
        time.sleep(2)
        assert self.driver.current_url == 'http://127.0.0.1:5000/'

    def test_story4_showsummary(self):
        assert False

    def test_story5_bookinfo(self):
        assert False

    def test_story6_booking_ok(self):
        self.test_story1_login_scenario1()
        field_book = self.driver.find_element(By.CLASS_NAME, "book_link")
        field_book.click()
        field_places = self.driver.find_element(By.ID, "number_of_places")
        field_places.send_keys("10")
        time.sleep(2)
        field_places.submit()
        assert "Great-booking complete!" in self.driver.page_source

    def test_story7_booking_more_available(self):
        # TODO : need to load a test database for assert more than
        # number of places in competition after more 12 test
        self.test_story1_login_scenario1()
        field_book = self.driver.find_element(By.CLASS_NAME, "book_link")
        field_book.click()
        field_places = self.driver.find_element(By.ID, "number_of_places")
        field_places.send_keys("25")
        time.sleep(2)
        field_places.submit()
        assert "Your club have not enough points"\
            in self.driver.page_source
        time.sleep(2)     
        assert False
        # TODO : need to load a test database for assert more than
        # number of places in competition

    def test_story7_booking_more_12(self):
        self.test_story1_login_scenario1()
        # try to book 20 places
        field_book = self.driver.find_element(By.CLASS_NAME, "book_link")
        field_book.click()
        field_places = self.driver.find_element(By.ID, "number_of_places")
        field_places.send_keys("20")
        time.sleep(2)
        field_places.submit()
        assert "You cannot book more than 12 places"\
            in self.driver.page_source
        # try to book 10 + 10 places
        field_places = self.driver.find_element(By.ID, "number_of_places")
        field_places.send_keys("10")
        time.sleep(2)
        field_places.submit()
        field_book = self.driver.find_element(By.CLASS_NAME, "book_link")
        field_book.click()
        field_places = self.driver.find_element(By.ID, "number_of_places")
        field_places.send_keys("10")
        time.sleep(2)
        field_places.submit()
        assert "You cannot book more than 12 places"\
            in self.driver.page_source

