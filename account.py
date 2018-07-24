import os
from selenium.webdriver.common.keys import Keys
USERNAME = os.environ.get('EZLUSER')
PASSWORD = os.environ.get('EZLPASSWORD')


def login(driver):
	username_el = driver.find_element_by_name('login')
	username_el.send_keys(USERNAME)
	password_el = driver.find_element_by_name('password')
	password_el.send_keys(PASSWORD)
	btn_logar_el = driver.find_element_by_tag_name
	list(filter(lambda i: i.text, driver.find_elements_by_tag_name('button')))[0].click()

