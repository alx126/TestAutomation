import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ActionChains, Keys


# from selenium.webdriver.firefox.service import Service
# from webdriver_manager.firefox import GeckoDriverManager


class Travels(unittest.TestCase):
    LINK = 'https://www.phptravels.net/'
    BUTTON_ACCOUNT = (By.CSS_SELECTOR, 'button#ACCOUNT')
    BUTTON_SIGNUP = (By.CSS_SELECTOR, 'button#button[type="submit"]')
    FLIGHT_DEPARTURE_FIELD = (By.CSS_SELECTOR, 'input#departure[class*="depart form-control"]')
    FLIGHT_RETURN_FIELD = (By.CSS_SELECTOR, 'input#return[name="returning"]')
    BUTTON_FLIGHT_SEARCH = (By.CSS_SELECTOR, 'button#flights-search')

    # def setUp(self):
    #     self.service = Service(GeckoDriverManager().install())
    #     self.driver = webdriver.Firefox(service=self.service)
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(2)

    def setUp(self):
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get(self.LINK)
        self.driver.maximize_window()
        time.sleep(1)
        self.driver.implicitly_wait(1)

    def tearDown(self):
        self.driver.quit()

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def click_Account(self):
        account_button = self.driver.find_element(self.BUTTON_ACCOUNT)
        ActionChains(self.driver).move_to_element(account_button).click().perform()
        self.driver.implicitly_wait(2)

    def get_calendar_month_year(self):
        lista_calendare = self.driver.find_elements(By.XPATH,
                                                    "//div[@class='datepicker dropdown-menu']/descendant::th[@class='switch']")
        for calendar in lista_calendare:
            if calendar.is_displayed():
                return calendar.text
        # return self.driver.find_element(locator).text

    def open_date_picker(self, locator):
        # if len(self.driver.find_elements(By.CLASS_NAME, "day")) == 0:
        self.driver.find_element(*locator).click()
        time.sleep(1)

    def insert_date(self, locator, date):
        self.driver.find_element(*locator).send_keys(Keys.CONTROL, 'a')
        self.driver.find_element(*locator).send_keys(date)

    def click_date_picker_next(self):
        next_button_list = self.driver.find_elements(By.CSS_SELECTOR, "th.next")
        for button in next_button_list:
            if button.is_displayed():
                button.click()

    def click_date_picker_prev(self):
        prev_button_list = self.driver.find_elements(By.CSS_SELECTOR, "th.prev")
        for button in prev_button_list:
            if button.is_displayed():
                button.click()

    def select_date(self, year, month, day, locator_datepicker):
        self.open_date_picker(locator_datepicker)
        self.get_calendar_month_year()
        while year not in self.get_calendar_month_year():
            self.click_date_picker_next()
        while month not in self.get_calendar_month_year():
            self.click_date_picker_next()
        days_list = self.driver.find_elements(By.XPATH, f"//td[@class='day ' and contains(text(), {day})]")
        for day in days_list:
            if day.is_displayed():
                day.click()

    # (By.XPATH,"//div[@class='datepicker dropdown-menu']/descendant::th[@class='switch']")
    # //td[@class='day' and contains(text(), 8)]

    def test_3_sign_in(self):
        # self.click_Account()
        account_button = self.driver.find_element(By.CSS_SELECTOR, 'button#ACCOUNT')
        ActionChains(self.driver).move_to_element(account_button).click().perform()
        # account_button = self.driver.find_element(self.BUTTON_ACCOUNT)
        # ActionChains(self.driver).move_to_element(account_button).click().perform()
        time.sleep(1)

        customer_login = self.driver.find_element(
            By.XPATH, "//div[@class='dropdown']/descendant::a[contains(text(), 'Customer Login')]")
        customer_login.click()
        time.sleep(1)

        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Email"]').send_keys('alex.popescu@gmail.com')
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Password"]').send_keys('P@ssw0rd')
        time.sleep(1)
        self.click((By.CSS_SELECTOR, 'label[for="rememberchb"]'))
        time.sleep(1)

        self.click((By.XPATH, "//button[@type='submit']/descendant::span[text()='Login']"))
        time.sleep(1)

        WebDriverWait(self.driver, 3).until(EC.url_contains('/account/dashboard'))
        time.sleep(1)

    # @unittest.skip
    def test_1_sign_up(self):

        account_button = self.driver.find_element(By.CSS_SELECTOR, 'button#ACCOUNT')
        ActionChains(self.driver).move_to_element(account_button).click().perform()
        time.sleep(1)

        customer_signup = self.driver.find_element(
            By.XPATH, "//div[@class='dropdown']/descendant::a[contains(text(), 'Customer Signup')]")
        customer_signup.click()
        self.driver.implicitly_wait(5)
        time.sleep(1)

        # ActionChains(self.driver).move_to_element(self.driver.find_element(
        #     By.CSS_SELECTOR, 'input[placeholder="First Name"]')).click().perform()
        # time.sleep(3)

        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="First Name"]').send_keys('Ale')
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="First Name"]').send_keys('x')
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Last Name"]').send_keys('Pop')
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Last Name"]').send_keys('escu')
        time.sleep(2)

        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Phone"]').send_keys('0211234123')
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Email"]').send_keys('alex.popescu@gmail.com')
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Password"]').send_keys('P@ssw0rd')
        time.sleep(2)

        # find the reCAPTCHA element and click on it
        WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it(
            (By.CSS_SELECTOR, "iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()
        time.sleep(10)

        # switch back to window content
        self.driver.switch_to.default_content()

        submit_button = WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'button#button[type="submit"]')))
        submit_button.click()
        time.sleep(1)

    # @unittest.skip
    def test_2_sign_up(self):
        # self.click_Account()
        account_button = self.driver.find_element(By.CSS_SELECTOR, 'button#ACCOUNT')
        ActionChains(self.driver).move_to_element(account_button).click().perform()
        # account_button = self.driver.find_element(self.BUTTON_ACCOUNT)
        # ActionChains(self.driver).move_to_element(account_button).click().perform()
        time.sleep(1)

        customer_login = self.driver.find_element(
            By.XPATH, "//div[@class='dropdown']/descendant::a[contains(text(), 'Customer Login')]")
        customer_login.click()
        time.sleep(1)

        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Email"]').send_keys('alex.popescu@gmail.com')

        self.click((By.CSS_SELECTOR, 'a[class*="btn-lg d-flex"]'))
        time.sleep(1)

        WebDriverWait(self.driver, 3).until(EC.url_contains('/signup'))
        time.sleep(2)

        # switch to re-captcha frame
        WebDriverWait(self.driver, 5).until(EC.frame_to_be_available_and_switch_to_it(
            (By.CSS_SELECTOR, "iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()
        time.sleep(5)

        # switch back to window content
        self.driver.switch_to.default_content()

        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="First Name"]').send_keys('Ale')
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="First Name"]').send_keys('x')
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Last Name"]').send_keys('Pop')
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Last Name"]').send_keys('escu')
        time.sleep(1)

        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Phone"]').send_keys('0211234123')
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Email"]').send_keys('alex.popescu@gmail.com')
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Password"]').send_keys('P@ssw0rd')
        time.sleep(1)

        self.driver.find_element(By.CSS_SELECTOR, 'button#button[type="submit"]').click()
        time.sleep(2)

    def test_4_search_flight(self):
        tab_flight = self.driver.find_element(By.ID, "flights-tab")
        tab_flight.click()
        time.sleep(1)

        radio_buton = self.driver.find_element(By.CSS_SELECTOR, 'input.form-check-input[id="round-trip"]')
        radio_buton.click()
        # time.sleep(1)

        fly_from = self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Flying From"]')
        fly_from.send_keys('Henri Coanda')
        # time.sleep(1)

        self.driver.find_element(By.XPATH, '//strong[contains(text(),"Henri Coanda")]').click()
        # time.sleep(1)

        fly_to = self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="To Destination"]')
        fly_to.send_keys('Frankfurt')
        # time.sleep(1)

        self.driver.find_element(By.XPATH, '//strong[contains(text()," Frankfurt Main")]').click()
        # time.sleep(1)

        self.open_date_picker(self.FLIGHT_DEPARTURE_FIELD)
        self.get_calendar_month_year()
        while "2024" not in self.get_calendar_month_year():
            self.click_date_picker_next()
        time.sleep(1)
        while "May 2023" not in self.get_calendar_month_year():
            self.click_date_picker_prev()
        time.sleep(1)

        # self.select_date("2023", "July", "12", self.FLIGHT_DEPARTURE_FIELD)
        # time.sleep(1)

        self.open_date_picker(self.FLIGHT_DEPARTURE_FIELD)
        self.insert_date(self.FLIGHT_DEPARTURE_FIELD, '08-07-2023')
        # self.driver.find_element(By.CSS_SELECTOR, 'input#departure[class*="depart form-control"]').send_keys('08-05-2023')
        time.sleep(1)

        self.open_date_picker(self.FLIGHT_RETURN_FIELD)
        self.insert_date(self.FLIGHT_RETURN_FIELD, '17-07-2023')
        time.sleep(1)

        self.click(self.BUTTON_FLIGHT_SEARCH)
        time.sleep(3)
