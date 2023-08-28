# import time
# import multiprocessing as mp
# from flask import Flask
# import urllib3
from flask_testing import LiveServerTestCase
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# from selenium.webdriver.edge.options import Options
# from selenium.webdriver.edge.service import Service
from gudlft.server import app


class TestAppStories(LiveServerTestCase):
    # mp.set_start_method('fork', force=True)

    def create_app(self):
        # mp.set_start_method('spawn')
        # app.test_client()
        # app = Flask(__name__)
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 8943
        app.config['LIVESERVER_TIMEOUT'] = 10
        return app

    # @classmethod
    # def setUpClass(cls):
    #     super().setUpClass()
    #     options = Options()
    #     options.use_chromium = True
    #     options.add_experimental_option(
    # 'excludeSwitches', ['enable-logging'])
    #     # options.add_argument('--headless')
    #     service = Service(
    #         executable_path="tests/fonctionnal/msedgedriver.exe"
    #         )

    #     cls.driver = webdriver.Edge(
    #         service=service,
    #         options=options,
    #         )
    #     cls.driver.implicitly_wait(10)
    #     # cls.url = cls.live_server_url
    #     super(TestAppStories, cls).setUpClass()

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()
    #     super(TestAppStories, cls).tearDownClass()

    def setUp(self):
        ...
        # options = Options()
        # options.use_chromium = True
        # options.add_experimental_option(
        # 'excludeSwitches', ['enable-logging'])
        # # options.add_argument('--headless')
        # service = Service(
        #     executable_path="tests/fonctionnal/msedgedriver.exe"
        #     )

        # self.driver = webdriver.Edge(
        #     service=service,
        #     options=options,
        #     )
        # # response = urllib3.urlopen(self.get_server_url())
        # # self.driver.get(self.get_server_url())

        # self.driver.minimize_window()
        # self.driver.maximize_window()

    def tearDown(self):
        # self.driver.quit()
        ...

    def test_story1_login_scenario1(self):
        """
        when: I enter my email and click "enter"
        then: the system show the summary page
        """
        assert False
        # self.driver.get(self.live_server_url)
        # field_email = self.driver.find_element(By.ID, "email_field")
        # field_email.send_keys("club@exemple.com")
        # time.sleep(2)
        # field_email.submit()
        # time.sleep(2)
        # assert "club@exemple.com" in self.driver.page_source
