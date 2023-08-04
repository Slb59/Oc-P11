import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service


class TestStories:

    def setup_method(self):
        # self.driver = webdriver.Edge("tests/fonctionnal_edge/msedgedriver.exe")
        options = Options()
        # options.binary_location = r"tests/fonctionnal_edge/msedgedriver.exe"
        # options = webdriver.EdgeOptions()
        options.use_chromium = True
        # options.add_argument('--allow-running-insecure-content')
        # options.add_argument("--ignore-certificate-errors")
        service = Service(executable_path="tests/fonctionnal_edge/msedgedriver.exe")
        self.driver = webdriver.Chrome(
            # service=service,
            options=options,
            executable_path=r"tests/fonctionnal_edge/msedgedriver.exe"
            # service=webdriver.edge.service.Service(executable_path="tests/fonctionnal_edge/msedgedriver.exe")
            )
        self.driver.get("http://127.0.0.1:5000/")
        self.driver.maximize_window()
        time.sleep(20)

    def teardown_method(self):
        self.driver.quit()

    def test_story1_login_scenario1():
        ...
    