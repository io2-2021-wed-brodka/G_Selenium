from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import random
import string

import admin_test

USER_TECH_ENDPOINT = "http://127.0.0.1:3000"


def testLoginUserPage():
	driver = webdriver.Firefox(executable_path="./geckodriver.exe")
	driver.get(f"{USER_TECH_ENDPOINT}/login")
	time.sleep(2)
	elem = driver.find_element_by_id(id_="login-login")
	elem.send_keys("tech")
	time.sleep(2)
	elem = driver.find_element_by_id(id_="login-password")
	elem.send_keys("tech")
	time.sleep(2)
	elem = driver.find_element_by_id(id_="login-button-confirm")
	elem.click()
	time.sleep(5)
	driver.quit()


def testLogoutUserPage():
	driver = webdriver.Firefox(executable_path="./geckodriver.exe")
	driver.get(f"{USER_TECH_ENDPOINT}/login")
	elem = driver.find_element_by_id(id_="login-login")
	elem.send_keys("tech")
	elem = driver.find_element_by_id(id_="login-password")
	elem.send_keys("tech")
	elem = driver.find_element_by_id(id_="login-button-confirm")
	elem.click()
	time.sleep(2)
	elem = driver.find_element_by_id(id_="logout-button-confirm")
	elem.click()
	time.sleep(5)
	driver.quit()


def testMalfunctionsAccessPage():
	driver = webdriver.Firefox(executable_path="./geckodriver.exe")
	driver.get(f"{USER_TECH_ENDPOINT}/login")
	elem = driver.find_element_by_id(id_="login-login")
	elem.send_keys("tech")
	elem = driver.find_element_by_id(id_="login-password")
	elem.send_keys("tech")
	elem = driver.find_element_by_id(id_="login-button-confirm")
	elem.click()
	time.sleep(1)
	elem = driver.find_element_by_id(id_="topbar-malfunctions")
	elem.click()
	time.sleep(20)
	driver.quit()


def testAll():
	if not admin_test.ADDED_TECH:
		admin_test.testAddTechPage()
	testLoginUserPage()
	testLogoutUserPage()
	testMalfunctionsAccessPage()


testAll()
