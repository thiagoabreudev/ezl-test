import os
from selenium.webdriver.common.keys import Keys
import time


def chat(driver):
	open_chat(driver)
	search_chat_company(driver)

def open_chat(driver):
	time.sleep(5)
	driver.find_element_by_xpath('/html/body/div[2]/nav/div/ul[1]/li[3]/a').click()
	time.sleep(5)
	driver.find_element_by_xpath('//*[@id="drop-title"]').click()

def search_chat_company(driver):
	search_el = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/section/div/div/div[1]/div[2]/div[2]/input')
	time.sleep(2)
	search_el.send_keys('')
