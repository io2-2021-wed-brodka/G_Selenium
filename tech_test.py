from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import random
import string

import admin_test

USER_TECH_ENDPOINT = "http://127.0.0.1:3000"


def testLoginTechPage():
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


def testLogoutTechPage():
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


def blockBikeTestPage():
	driver = webdriver.Firefox(executable_path="./geckodriver.exe")
	driver.get(f"{USER_TECH_ENDPOINT}/login")
	elem = driver.find_element_by_id(id_="login-login")
	elem.send_keys("tech")
	elem = driver.find_element_by_id(id_="login-password")
	elem.send_keys("tech")
	elem = driver.find_element_by_id(id_="login-button-confirm")
	elem.click()
	time.sleep(1)
	elem = driver.find_element_by_id(id_="topbar-bikes")
	elem.click()
	time.sleep(2)
	elem = driver.find_element_by_id(id_="bikes-block-0")
	elem.click()
	time.sleep(2)
	elem = driver.find_element_by_id(id_="bikes-block-confirm")
	elem.click()
	time.sleep(2)
	driver.close()


def unblockBikeTestPage():
	driver = webdriver.Firefox(executable_path="./geckodriver.exe")
	driver.get(f"{USER_TECH_ENDPOINT}/login")
	elem = driver.find_element_by_id(id_="login-login")
	elem.send_keys("tech")
	elem = driver.find_element_by_id(id_="login-password")
	elem.send_keys("tech")
	elem = driver.find_element_by_id(id_="login-button-confirm")
	elem.click()
	time.sleep(1)
	elem = driver.find_element_by_id(id_="topbar-bikes")
	elem.click()
	elem = driver.find_element_by_id(id_="bikes-block-0")
	elem.click()
	elem = driver.find_element_by_id(id_="bikes-block-confirm")
	elem.click()
	time.sleep(2)
	elem = driver.find_element_by_id(id_="bikes-switch-blocked")
	time.sleep(2)
	elem = driver.find_element_by_id(id_="bikes-unblock-0")
	elem.click()
	time.sleep(2)
	elem = driver.find_element_by_id(id_="bikes-unblock-confirm")
	elem.click()
	time.sleep(2)
	driver.close()



def testAll():
	if not admin_test.ADDED_TECH:
		admin_test.testAddTechPage()
	testLoginTechPage()
	testLogoutTechPage()
	testMalfunctionsAccessPage()
	blockBikeTestPage()
	unblockBikeTestPage()


testAll()
