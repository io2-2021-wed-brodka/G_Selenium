import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

SHOW_BROWSER = True  # TODO(tkarwowski): move to env
ADMIN_ENDPOINT = "http://127.0.0.1:3000"
USER_TECH_ENDPOINT = "http://127.0.0.1:3001"


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
        cls.random_login = "easy_login"

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

    def test_register(self):
        self.browser.get(f"{ADMIN_ENDPOINT}/login")
        self.wait_a_little(2)
        elem = self.browser.find_element_by_id(id_="sign-up-container")
        elem.click()
        self.wait_a_little(2)
        elem = self.browser.find_element_by_id(id_="register-login")
        elem.send_keys(self.random_login)
        self.wait_a_little(2)
        elem = self.browser.find_element_by_id(id_="register-password")
        elem.send_keys("newPassword")
        self.wait_a_little(1)
        elem = self.browser.find_element_by_id(id_="register-button-confirm")
        elem.click()
        self.wait_a_little(5)

    def testLoginUserPage(self):
        self.browser.get(f"{USER_TECH_ENDPOINT}/login")
        self.wait_a_little(2)
        elem = self.browser.find_element_by_id(id_="login-login")
        elem.send_keys(self.random_login)
        self.wait_a_little(2)
        elem = self.browser.find_element_by_id(id_="login-password")
        elem.send_keys("newPassword")
        self.wait_a_little(2)
        elem = self.browser.find_element_by_id(id_="login-button-confirm")
        elem.click()
        self.wait_a_little(5)

    def testLogoutUserPage(self):
        self.browser.get(f"{USER_TECH_ENDPOINT}/login")
        elem = self.browser.find_element_by_id(id_="login-login")
        elem.send_keys(self.random_login)
        elem = self.browser.find_element_by_id(id_="login-password")
        elem.send_keys("newPassword")
        elem = self.browser.find_element_by_id(id_="login-button-confirm")
        elem.click()
        self.wait_a_little(2)
        elem = self.browser.find_element_by_id(id_="logout-button-confirm")
        elem.click()
        self.wait_a_little(5)

    def testViewStationListUser(self):
        self.browser.get(f"{USER_TECH_ENDPOINT}/login")
        elem = self.browser.find_element_by_id(id_="login-login")
        elem.send_keys(self.random_login)
        elem = self.browser.find_element_by_id(id_="login-password")
        elem.send_keys("newPassword")
        elem = self.browser.find_element_by_id(id_="login-button-confirm")
        elem.click()
        elem = self.browser.find_element_by_id(id_="topbar-station-button-confirm")
        elem.click()
        self.wait_a_little(5)

    def testViewBikeListUser(self):
        self.browser.get(f"{USER_TECH_ENDPOINT}/login")
        elem = self.browser.find_element_by_id(id_="login-login")
        elem.send_keys(self.random_login)
        elem = self.browser.find_element_by_id(id_="login-password")
        elem.send_keys("newPassword")
        elem = self.browser.find_element_by_id(id_="login-button-confirm")
        elem.click()
        elem = self.browser.find_element_by_id(id_="topbar-station-button-confirm")
        elem.click()
        self.wait_a_little(2)
        elem = self.browser.find_element_by_id(id_="station-button-confirm-0")
        elem.click()
        self.wait_a_little(5)

    def testRentBiketUser(self):
        elem = self.browser.find_element_by_id(id_="login-login")
        elem.send_keys(self.random_login)
        elem = self.browser.find_element_by_id(id_="login-password")
        elem.send_keys("newPassword")
        elem = self.browser.find_element_by_id(id_="login-button-confirm")
        elem.click()
        elem = self.browser.find_element_by_id(id_="topbar-station-button-confirm")
        elem.click()
        elem = self.browser.find_element_by_id(id_="station-button-confirm-2")
        elem.click()
        self.wait_a_little(1)
        elem = self.browser.find_element_by_id(id_="bike-rent-button-confirm-0")
        elem.click()
        self.wait_a_little(1)
        elem = self.browser.find_element_by_id(id_="bike-rent-button-confirm")
        elem.click()
        self.wait_a_little(5)

    def testReturnBiketUser(self):
        self.browser.get(f"{USER_TECH_ENDPOINT}/login")
        elem = self.browser.find_element_by_id(id_="login-login")
        elem.send_keys(self.random_login)
        elem = self.browser.find_element_by_id(id_="login-password")
        elem.send_keys("newPassword")
        elem = self.browser.find_element_by_id(id_="login-button-confirm")
        elem.click()
        elem = self.browser.find_element_by_id(id_="topbar-station-button-confirm")
        elem.click()
        elem = self.browser.find_element_by_id(id_="station-button-confirm-2")
        elem.click()
        elem = self.browser.find_element_by_id(id_="bike-rent-button-confirm-0")
        elem.click()
        elem = self.browser.find_element_by_id(id_="bike-rent-button-confirm")
        elem.click()
        self.wait_a_little(1)
        elem = self.browser.find_element_by_id(id_="topbar-rented-button-confirm")
        elem.click()
        self.wait_a_little(1)
        elem = self.browser.find_element_by_id(id_="return-bike-button-0")
        elem.click()
        self.wait_a_little(1)
        stationListSelect = Select(self.browser.find_element_by_id(id_="select-return-bike-station"))
        stationListSelect.select_by_visible_text("Uniwersytet")
        self.wait_a_little(1)
        elem = self.browser.find_element_by_id(id_="dialog-return-bike-button-confirm")
        elem.click()
        self.wait_a_little(5)


if __name__ == '__main__':
    unittest.main()
