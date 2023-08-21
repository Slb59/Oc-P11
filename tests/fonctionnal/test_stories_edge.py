import time
import pytest

from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("driver_edge_init")
class TestStories:
    """
    For each test, the system open an edge browser
    and connect to the 127.0.0.1:500 page
    """

    def test_story1_login_scenario1(self):
        """
        when: I enter my email and click "enter"
        then: the system show the summary page
        """
        field_email = self.driver.find_element(By.ID, "email_field")
        field_email.send_keys("club@exemple.com")
        time.sleep(2)
        field_email.submit()
        time.sleep(2)
        assert "club@exemple.com" in self.driver.page_source

    def test_story2_login_scanario2(self):
        """
        when: I indicate an email not recognized in the club database and that
        I click on "Enter"
        then: the system tells me a message "Sorry, that email wasn't found."
        """
        field_email = self.driver.find_element(By.ID, "email_field")
        field_email.send_keys("unlonown@example.com")
        time.sleep(2)
        field_email.submit()
        time.sleep(2)
        assert "Cette adresse email n'est pas reconnue"\
            in self.driver.page_source

    def test_story3_logout_from_summary(self):
        """
        when: I am logged in and in the summary page and that
        I click on "logout" button
        then:  the system directs me to the home page
        and I am disconnected from the system.
        """
        self.test_story1_login_scenario1()
        field_logout = self.driver.find_element(By.CLASS_NAME, "logout_link")
        field_logout.click()
        assert self.driver.current_url == 'http://127.0.0.1:5000/'

    def test_story3_logout_from_book(self):
        """
        when: I am logged in and in the book page and that
        I click on "logout" button
        then:  the system directs me to the home page
        and I am disconnected from the system.
        """
        self.test_story1_login_scenario1()
        field_book = self.driver.find_element(By.CLASS_NAME, "book_link")
        field_book.click()
        field_logout = self.driver.find_element(By.CLASS_NAME, "logout_link")
        field_logout.click()
        time.sleep(2)
        assert self.driver.current_url == 'http://127.0.0.1:5000/'

    def test_story4_showsummary(self):
        """
        when: Since I am logged in and I am on The "summary" page
        then: I can view the balance of my current points and
        the list of competitions ordered by decrease date
        """
        self.test_story1_login_scenario1()
        time.sleep(3)
        assert "Points available: 10" in self.driver.page_source
        data = self.driver.page_source
        data_list = [y for y in (x.strip() for x in data.splitlines()) if y]
        # print(data_list)
        try:
            i1 = data_list.index('<h3>List of upcoming competitions:</h3>')
            i2 = data_list.index('Test competition3<br>')
            i3 = data_list.index('Test competition2<br>')
            i4 = data_list.index('<h3> List of past competitions:</h3>')            
            i5 = data_list.index('Test competition<br>')
            i6 = data_list.index('Test competition4<br>')
        except ValueError:
            assert False
        assert i1 < i2 and i2 < i3 and i3 < i4 and i4 < i5 and i5 < i6

    def test_story5_bookinfo(self):
        assert False

    def test_story6_booking_ok(self):
        """
        When: I indicate the number of places
        I want to reserve and click on the "book" button
        Then: The system directs me to the summary page
        and tells me a message confirming the number of
        points purchased and my booking is correctly registered
        """
        self.test_story1_login_scenario1()
        field_book = self.driver.find_element(By.CLASS_NAME, "book_link")
        field_book.click()
        field_places = self.driver.find_element(By.ID, "number_of_places")
        field_places.send_keys("10")
        time.sleep(2)
        field_places.submit()
        assert "Great-booking complete!" in self.driver.page_source

    def test_story7_booking_more_available(self):
        """
        When: I indicate a number greater than number
        of places avalaible
        Then : the system displays an error message and me
        directs to the summary page and none change is not
        save in the system
        """
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

    def test_story8_booking_more_12(self):
        """
        When : I indicate a number greater than 12
        Then: The system displays an error message
        and directs me to the summary page and no changes
        are saved in the system
        """
        field_email = self.driver.find_element(By.ID, "email_field")
        field_email.send_keys("club2@exemple.com")
        field_email.submit()
        # try to book 20 places
        field_book = self.driver.find_element(By.CLASS_NAME, "book_link")
        field_book.click()
        field_places = self.driver.find_element(By.ID, "number_of_places")
        field_places.send_keys("20")
        time.sleep(2)
        field_places.submit()
        # print(self.driver.page_source)
        assert "You cannot purchase more than 12 places"\
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
        # print(self.driver.page_source)
        assert "You cannot purchase more than 12 places"\
            in self.driver.page_source

    def test_story9_displayboard(self):
        """
        When I am not logged and I am on then home page
        Then The system displays the liste of other clubs
        and their points
        """
        field_book = self.driver.find_element(By.CLASS_NAME, "board_link")
        field_book.click()
        data = self.driver.page_source
        data_list = [y for y in (x.strip() for x in data.splitlines()) if y]
        time.sleep(2)
        try:
            i1 = data_list.index('club for test <br>')
            i2 = data_list.index('club for test2 <br>')
            i3 = data_list.index('club for test3 <br>')
        except ValueError:
            assert False
        assert i1 < i2 and i2 < i3
