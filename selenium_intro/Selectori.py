import time

from selenium import webdriver

driver = webdriver.Chrome()

LINK = "https://formy-project.herokuapp.com"

driver.get(LINK)
time.sleep(1)

driver.maximize_window()
time.sleep(1)


