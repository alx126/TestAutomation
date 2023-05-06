import time

from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

LINK_dev = "https://o360webdevkl.azurewebsites.net/"

driver.get(LINK_dev)
time.sleep(1)
driver.maximize_window()
time.sleep(3)

# login_Engsys = driver.find_element(By.CSS_SELECTOR, 'button.accountButton.firstButton[id="EngSys"]')
# login_Engsys.click()
# time.sleep(3)
def sign_in_admin():
    driver.find_element(By.CSS_SELECTOR, 'input#logonIdentifier').send_keys('admin@engsys360dev.onmicrosoft.com')
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, 'input#password').send_keys('Es2K-Es2K')
    time.sleep(1)
    login_Admin = driver.find_element(By.CSS_SELECTOR, 'button#next')
    login_Admin.click()
    time.sleep(1)

def sign_in_Engsys():
    driver.find_element(By.CSS_SELECTOR, 'input#logonIdentifier').send_keys('admin@engsys360dev.onmicrosoft.com')
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, 'input#password').send_keys('Es2K-Es2K')
    time.sleep(1)
    login_EngSys = driver.find_element(By.CSS_SELECTOR, 'button#EngSys')
    login_EngSys.click()
    time.sleep(1)


# sign_in_admin()
# time.sleep(3)
sign_in_Engsys()
time.sleep(3)

