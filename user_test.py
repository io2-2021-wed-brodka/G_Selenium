from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import random
import string

USER_TECH_ENDPOINT = "http://127.0.0.1:3000"

random_login = "easy_login"
def testBikeNumberOnStationPage():
	driver = webdriver.Firefox(executable_path="./geckodriver.exe")
	driver.get(f"{USER_TECH_ENDPOINT}/login")
	elem = driver.find_element_by_id(id_="login-login")
	elem.send_keys(random_login)
	elem = driver.find_element_by_id(id_="login-password")
	elem.send_keys("newPassword")
	elem = driver.find_element_by_id(id_="login-button-confirm")
	elem.click()
	time.sleep(1)
	elem = driver.find_element_by_id(id_="topbar-station-button-confirm")
	elem.click()
	time.sleep(20)
	driver.quit()


def sendMalfunctionPage():
	driver = webdriver.Firefox(executable_path="./geckodriver.exe")
	driver.get(f"{USER_TECH_ENDPOINT}/login")
	elem = driver.find_element_by_id(id_="login-login")
	elem.send_keys(random_login)
	elem = driver.find_element_by_id(id_="login-password")
	elem.send_keys("newPassword")
	elem = driver.find_element_by_id(id_="login-button-confirm")
	elem.click()
	elem = driver.find_element_by_id(id_="topbar-station-button-confirm")
	elem.click()
	elem = driver.find_element_by_id(id_="station-button-confirm-2")
	elem.click()
	elem = driver.find_element_by_id(id_="bike-rent-button-confirm-0")
	elem.click()
	elem = driver.find_element_by_id(id_="bike-rent-button-confirm")
	elem.click()
	time.sleep(2)
	elem = driver.find_element_by_id(id_="bike-create-malfunction-0")
	elem.click()
	time.sleep(2)
	elem = driver.find_element_by_id(id_="bike-create-malfunction-desc")
	elem.send_keys("Przerzutka sie blokuje")
	time.sleep(2)
	elem = driver.find_element_by_id(id_="bike-create-malfunction-confirm")
	elem.click()
	time.sleep(2)
	driver.quit()

def testReserveBiketUserPage():
    driver = webdriver.Firefox(executable_path="./geckodriver.exe")
    driver.get(f"{USER_TECH_ENDPOINT}/login")
    elem = driver.find_element_by_id(id_="login-login")
    elem.send_keys(random_login)
    elem = driver.find_element_by_id(id_="login-password")
    elem.send_keys("newPassword")
    elem = driver.find_element_by_id(id_="login-button-confirm")
    elem.click()
    elem = driver.find_element_by_id(id_="topbar-station-button-confirm")
    elem.click()
    elem = driver.find_element_by_id(id_="station-button-confirm-2")
    elem.click()
    time.sleep(1)
    elem = driver.find_element_by_id(id_="bike-reserve-button-confirm-0")
    elem.click()
    time.sleep(1)
    elem = driver.find_element_by_id(id_="bike-reserve-button-confirm")
    elem.click()
    time.sleep(2100) #waiting for automatic decay
    driver.refresh()
    time.sleep(10)
    driver.quit()


def testCancelReservationBikeUserPage():
    driver = webdriver.Firefox(executable_path="./geckodriver.exe")
    driver.get(f"{USER_TECH_ENDPOINT}/login")
    elem = driver.find_element_by_id(id_="login-login")
    elem.send_keys(random_login)
    elem = driver.find_element_by_id(id_="login-password")
    elem.send_keys("newPassword")
    elem = driver.find_element_by_id(id_="login-button-confirm")
    elem.click()
    elem = driver.find_element_by_id(id_="topbar-station-button-confirm")
    elem.click()
    elem = driver.find_element_by_id(id_="station-button-confirm-2")
    elem.click()
    elem = driver.find_element_by_id(id_="bike-reserve-button-confirm-0")
    elem.click()
    elem = driver.find_element_by_id(id_="bike-reserve-button-confirm")
    elem.click()
    time.sleep(1)
    elem = driver.find_element_by_id(id_="topbar-reserved")
    elem.click()
    time.sleep(1)
    elem = driver.find_element_by_id(id_="cancel-reservation-0")
    elem.click()
    time.sleep(1)
    elem = driver.find_element_by_id(id_="cancel-reservation-confirm")
    elem.click()
    time.sleep(5)
    driver.quit()

#this test needs blocked user with:
# login: blocked
# pass: blocked
def blockedUserReturnPage():
	driver = webdriver.Firefox(executable_path="./geckodriver.exe")
	driver.get(f"{USER_TECH_ENDPOINT}/login")
	elem = driver.find_element_by_id(id_="login-login")
	elem.send_keys("blocked")
	elem = driver.find_element_by_id(id_="login-password")
	elem.send_keys("blocked")
	elem = driver.find_element_by_id(id_="login-button-confirm")
	elem.click()
	time.sleep(1)
	elem = driver.find_element_by_id(id_="topbar-rented-button-confirm")
	elem.click()
	time.sleep(2)
	elem = driver.find_element_by_id(id_="return-bike-button-0")
	elem.click()
	time.sleep(2)
	stationListSelect = Select(driver.find_element_by_id(id_="select-return-bike-station"))
	stationListSelect.select_by_visible_text("Uniwersytet")
	time.sleep(2)
	elem = driver.find_element_by_id(id_="dialog-return-bike-button-confirm")
	elem.click()
	time.sleep(5)
	driver.quit()



def testAll():
	testBikeNumberOnStationPage()
	sendMalfunctionPage()
	#blockedUserReturnPage()
	testReserveBiketUserPage()
	testCancelReservationBikeUserPage()
