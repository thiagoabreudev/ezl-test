from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from account import login

driver = webdriver.Firefox()
driver.get("http://localhost:8000")

login(driver)