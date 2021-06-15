from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import random
import string

USER_TECH_ENDPOINT = "http://127.0.0.1:3000"

random_login = "easy_login"
def testBikeReservation():
	driver = webdriver.Firefox(executable_path="./geckodriver.exe")
	driver.get("http://localhost:3000/login")
	elem = driver.find_element_by_id(id_="login-login")
	elem.send_keys(random_login)
	elem = driver.find_element_by_id(id_="login-password")
	elem.send_keys("newPassword")
	elem = driver.find_element_by_id(id_="login-button-confirm")
	elem.click()
	elem = driver.find_element_by_id(id_="topbar-reserved")
	elem.click()

	driver.quit()