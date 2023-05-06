import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains, Keys


class SwagLabs(unittest.TestCase):
    LINK = "https://www.saucedemo.com/"

    BUTTON_LOGIN = (By.ID, 'login-button')
    FIELD_USERNAME = (By.ID, 'user-name')
    FIELD_PASSWORD = (By.ID, 'password')

    LOGIN_USERS_LIST = (By.ID, 'login_credentials')
    LOGIN_PASS_LIST = (By.CLASS_NAME, 'login_password')
    LOGIN_USER_STD_ELEM = (By.XPATH, '//*[@id="login_credentials"]/text()[1]')
    LOGIN_PASSWORD_ELEM = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/text()')
    LOGIN_USER_STD = 'standard_user'
    LOGIN_PASSWORD = 'secret_sauce'

    LOGIN_ERROR = (By.CSS_SELECTOR, 'h3[data-test="error"]')
    ERROR_REQ_USER = 'Epic sadface: Username is required'
    ERROR_REQ_PASS = 'Epic sadface: Password is required'
    ERROR_CREDENTIALS_MISSMATCH = 'Epic sadface: Username and password do not match any user in this service'

    def setUp(self):
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get(self.LINK)
        self.driver.maximize_window()
        self.driver.implicitly_wait(1)

    def tearDown(self):
        self.driver.quit()

    def find(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.find(locator).click()

    def click_button_login(self):
        self.click(self.BUTTON_LOGIN)

    def write(self, locator, text):
        self.find(locator).send_keys(text)

    def select_and_overwrite(self, locator, text):
        field = self.find(locator)
        field.send_keys(Keys.CONTROL, "a")
        field.send_keys(Keys.BACKSPACE)
        field.send_keys(text)

    def login(self, user, password):
        self.select_and_overwrite(self.FIELD_USERNAME, user)
        self.select_and_overwrite(self.FIELD_PASSWORD, password)
        self.click_button_login()
        self.driver.implicitly_wait(2)

    #@unittest.skip
    def test_1_find_credentials(self):
        users_list = self.find(self.LOGIN_USERS_LIST).text.split()
        pass_list = self.find(self.LOGIN_PASS_LIST).text.split()

        for password in pass_list:
            for user in users_list:
                self.login(user, password)
                if len(self.driver.find_elements(*self.LOGIN_ERROR)) > 0:
                    print(f'Username: "{user}" and password: "{password}" are not accepted.')
                    #time.sleep(1)
                else:
                    print(f'Username "{user}" is accepted.')
                    print(f'Password "{password}" is accepted.')
                    break

        expected_url = 'https://www.saucedemo.com/inventory.html'
        self.assertTrue(self.driver.current_url == expected_url)

    def test_2_login_username_required(self):
        self.click_button_login()
        self.assertEqual(self.find(self.LOGIN_ERROR).text, self.ERROR_REQ_USER)

    def test_3_login_password_required(self):
        self.write(self.FIELD_USERNAME, self.LOGIN_USER_STD)
        self.click_button_login()
        self.assertEqual(self.find(self.LOGIN_ERROR).text, self.ERROR_REQ_PASS)

    def test_4_login_credentials_missmatch(self):
        self.write(self.FIELD_USERNAME, 'blabla')
        self.write(self.FIELD_PASSWORD, 'blabla')
        self.click_button_login()
        self.assertEqual(self.find(self.LOGIN_ERROR).text, self.ERROR_CREDENTIALS_MISSMATCH)

    def test_5_login_wrong_username(self):
        self.write(self.FIELD_USERNAME, 'blabla')
        self.write(self.FIELD_PASSWORD, self.LOGIN_PASSWORD)
        self.click_button_login()
        self.assertEqual(self.find(self.LOGIN_ERROR).text, self.ERROR_CREDENTIALS_MISSMATCH)

    def test_6_login_wrong_password(self):
        self.write(self.FIELD_USERNAME, self.LOGIN_USER_STD)
        self.write(self.FIELD_PASSWORD, 'blabla')
        self.click_button_login()
        self.assertEqual(self.find(self.LOGIN_ERROR).text, self.ERROR_CREDENTIALS_MISSMATCH)

    def test_7_login(self):
        self.login(self.LOGIN_USER_STD, self.LOGIN_PASSWORD)
        expected_url = 'https://www.saucedemo.com/inventory.html'
        actual_url = self.driver.current_url
        self.assertTrue(actual_url == expected_url)
