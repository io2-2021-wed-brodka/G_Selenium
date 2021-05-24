import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait

SHOW_BROWSER = True  # TODO(tkarwowski): move to env
ADMIN_ENDPOINT = "http://127.0.0.1:8080"
USER_TECH_ENDPOINT = "http://127.0.0.1:8081"


class SeleniumAdminTest(unittest.TestCase):
    browser = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        firefox_options = Options()
        if not SHOW_BROWSER:
            firefox_options.add_argument("--headless")
        firefox_options.add_argument("--window-size=1200,800")
        cls.browser = webdriver.Firefox(
            executable_path="./geckodriver", options=firefox_options
        )
        cls.browser.delete_all_cookies()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.browser.quit()

    def wait_until_element_found(self, xpath):
        WebDriverWait(self.browser, timeout=10).until(
            lambda x: self.browser.find_element_by_xpath(xpath)
        )

    def wait_a_little(self, seconds=2):
        if SHOW_BROWSER:
            sleep(seconds)

    def test_login(self):
        self.wait_a_little()
        self.browser.get(f"{ADMIN_ENDPOINT}/login")
        # wait untill page shows up

        # insert login

        # insert password

        # press LOG IN button

        # asset redirects to
        self.wait_a_little()
        self.wait_until_element_found("//span[.='LOGIN']")
        self.wait_a_little()
        element = self.browser.find_element_by_xpath("//span[.='LOGIN']")
        self.wait_a_little()

    # test case function to check the Person.get_name function
    def test_1_get_name(self):
        print("\nStart get_name test\n")
        print("\nFinish get_name test\n")


if __name__ == '__main__':
    unittest.main()
