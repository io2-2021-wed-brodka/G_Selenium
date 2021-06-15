import unittest
import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

SHOW_BROWSER = True  # TODO(tkarwowski): move to env
ADMIN_ENDPOINT = "http://127.0.0.1:3001"
USER_TECH_ENDPOINT = "http://127.0.0.1:3000"
station_name = ""


def testLoginAdminPage():
	driver = webdriver.Firefox(executable_path="./geckodriver.exe")
	driver.get(f"{ADMIN_ENDPOINT}/login")
	time.sleep(2)
	elem = driver.find_element_by_id(id_="login-login")
	elem.send_keys("admin")
	time.sleep(2)
	elem = driver.find_element_by_id(id_="login-password")
	elem.send_keys("admin")
	time.sleep(2)
	elem = driver.find_element_by_id(id_="login-button-confirm")
	elem.click()
	time.sleep(5)
	driver.quit()


def testLogoutAdminPage():
	driver = webdriver.Firefox(executable_path="./geckodriver.exe")
	driver.get(f"{ADMIN_ENDPOINT}/login")
	elem = driver.find_element_by_id(id_="login-login")
	elem.send_keys("admin")
	elem = driver.find_element_by_id(id_="login-password")
	elem.send_keys("admin")
	time.sleep(2)
	elem = driver.find_element_by_id(id_="login-button-confirm")
	elem.click()
	time.sleep(2)
	elem = driver.find_element_by_id(id_="logout-button-confirm")
	elem.click()
	time.sleep(5)
	driver.quit()


def testAddStationPage():
	driver = webdriver.Firefox(executable_path="./geckodriver.exe")
	driver.get(f"{ADMIN_ENDPOINT}/login")
	elem = driver.find_element_by_id(id_="login-login")
	elem.send_keys("admin")
	elem = driver.find_element_by_id(id_="login-password")
	elem.send_keys("admin")
	elem = driver.find_element_by_id(id_="login-button-confirm")
	elem.click()
	time.sleep(2)
	elem = driver.find_element_by_id(id_="topbar-stations")
	elem.click()
	time.sleep(2)
	elem = driver.find_element_by_id(id_="stations-new")
	elem.click()
	# main add station
	station_name = "Palisadowa"
	# later
	driver.quit()


def testRemoveStationPage():
	driver = webdriver.Firefox(executable_path="./geckodriver.exe")
	driver.get(f"{ADMIN_ENDPOINT}/login")
	elem = driver.find_element_by_id(id_="login-login")
	elem.send_keys("admin")
	elem = driver.find_element_by_id(id_="login-password")
	elem.send_keys("admin")
	time.sleep(2)
	elem = driver.find_element_by_id(id_="topbar-stations")
	elem.click()
	time.sleep(2)
	elem = driver.find_element_by_id(id_="stations-new")
	elem.click()
	driver.quit()


def testBlockStationPage():
	driver = webdriver.Firefox(executable_path="./geckodriver.exe")
	driver.get(f"{ADMIN_ENDPOINT}/login")
	elem = driver.find_element_by_id(id_="login-login")
	elem.send_keys("admin")
	elem = driver.find_element_by_id(id_="login-password")
	elem.send_keys("admin")
	time.sleep(1)
	elem = driver.find_element_by_id(id_="topbar-stations")
	elem.click()
	time.sleep(2)
	elem = driver.find_element_by_id(id_="stations-block-confirm-2")
	elem.click()
	time.sleep(2)
	driver.quit()


def testUnblockStationPage():
	driver = webdriver.Firefox(executable_path="./geckodriver.exe")
	driver.get(f"{ADMIN_ENDPOINT}/login")
	elem = driver.find_element_by_id(id_="login-login")
	elem.send_keys("admin")
	elem = driver.find_element_by_id(id_="login-password")
	elem.send_keys("admin")
	time.sleep(1)
	elem = driver.find_element_by_id(id_="topbar-stations")
	elem.click()
	elem = driver.find_element_by_id(id_="stations-block-confirm-2")
	elem.click()
	elem = driver.find_element_by_id(id_="stations-switch-blocked")
	elem.click()
	time.sleep(2)
	elem = driver.find_element_by_id(id_="stations-unblock-confirm-0")
	elem.click()
	time.sleep(2)


def testDetailStationPage():
	driver = webdriver.Firefox(executable_path="./geckodriver.exe")
	driver.get(f"{ADMIN_ENDPOINT}/login")
	elem = driver.find_element_by_id(id_="login-login")
	elem.send_keys("admin")
	elem = driver.find_element_by_id(id_="login-password")
	elem.send_keys("admin")
	time.sleep(1)
	elem = driver.find_element_by_id(id_="topbar-stations")
	elem.click()
	time.sleep(20)
	driver.quit()


def testDetailBikePage():
	driver = webdriver.Firefox(executable_path="./geckodriver.exe")
	driver.get(f"{ADMIN_ENDPOINT}/login")
	elem = driver.find_element_by_id(id_="login-login")
	elem.send_keys("admin")
	elem = driver.find_element_by_id(id_="login-password")
	elem.send_keys("admin")
	time.sleep(1)
	elem = driver.find_element_by_id(id_="topbar-stations")
	elem.click()
	time.sleep(20)
	driver.quit()


def testUserListPage():
	driver = webdriver.Firefox(executable_path="./geckodriver.exe")
	driver.get(f"{ADMIN_ENDPOINT}/login")
	elem = driver.find_element_by_id(id_="login-login")
	elem.send_keys("admin")
	elem = driver.find_element_by_id(id_="login-password")
	elem.send_keys("admin")
	time.sleep(1)
	elem = driver.find_element_by_id(id_="topbar-users")
	elem.click()
	time.sleep(20)
	driver.quit()


def testBlockUserPage():
	driver = webdriver.Firefox(executable_path="./geckodriver.exe")
	driver.get(f"{ADMIN_ENDPOINT}/login")
	elem = driver.find_element_by_id(id_="login-login")
	elem.send_keys("admin")
	elem = driver.find_element_by_id(id_="login-password")
	elem.send_keys("admin")
	time.sleep(1)
	elem = driver.find_element_by_id(id_="topbar-users")
	elem.click()
	elem = driver.find_element_by_id(id_="users-block-confirm-0")
	elem.click()
	time.sleep(2)
	driver.quit()


def testUnblockUserPage():
	driver = webdriver.Firefox(executable_path="./geckodriver.exe")
	driver.get(f"{ADMIN_ENDPOINT}/login")
	elem = driver.find_element_by_id(id_="login-login")
	elem.send_keys("admin")
	elem = driver.find_element_by_id(id_="login-password")
	elem.send_keys("admin")
	time.sleep(1)
	elem = driver.find_element_by_id(id_="topbar-users")
	elem.click()
	elem = driver.find_element_by_id(id_="users-block-confirm-0")
	elem.click()
	elem = driver.find_element_by_id(id_="stations-switch-blocked")
	elem.click()
	time.sleep(2)
	elem = driver.find_element_by_id(id_="stations-unblock-confirm-0")
	elem.click()
	time.sleep(2)
	driver.quit()


def testAllPage():
	testLoginAdminPage()
	testLogoutAdminPage()
	testAddStationPage()
	testRemoveStationPage()
	testBlockStationPage()
	testUnblockStationPage()
	#testAddBikePage()
	#testRemoveBikePage()
	testDetailStationPage()
	testDetailBikePage()
	testUserListPage()
	testBlockUserPage()
	testUnblockUserPage()
	#testAddTechPage()
	#testRemoveTechPage()

testAll()