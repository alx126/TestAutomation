import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class Practice_tests_Chrome(unittest.TestCase):
    LINK = 'https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver'
    BUTTON_ALERT = (By.CSS_SELECTOR, 'button#alert')
    BUTTON_CHANGE_TEXT = (By.CSS_SELECTOR, 'button#populate-text')
    BUTTON_DISPLAY_BUTTON = (By.CSS_SELECTOR, 'button#display-other-button')
    BUTTON_CHECKBOX = (By.CSS_SELECTOR, 'button#checkbox')
    BUTTON_ENABLE = (By.CSS_SELECTOR, 'button#enable-button')

    def setUp(self):
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get(self.LINK)
        self.driver.maximize_window()
        #time.sleep(1)
        self.driver.implicitly_wait(1)

    def tearDown(self):
        self.driver.quit()

    def click(self, locator):
        self.driver.find_element(*locator).click()

    #@unittest.skip
    def test_1_click_to_open_alert(self):
        self.click(self.BUTTON_ALERT)

        alert = WebDriverWait(self.driver, 6).until(EC.alert_is_present())
        alert.accept()
        alert_count =self.driver.find_element(By.XPATH,'//span[@id="alertcount"]') #//span[@id="alertcount" and contains(text(),'0')]

        self.assertTrue(alert_count.text == "0")

    def test_2_change_text(self):
        self.click(self.BUTTON_CHANGE_TEXT)
        WebDriverWait(self.driver, 11).until(
            EC.visibility_of_element_located((By.XPATH, '//h2[@class="target-text" and text()="Selenium Webdriver"]')))

        # expected_text = 'Selenium Webdriver'
        # self.driver.implicitly_wait(11)
        # target = self.driver.find_element(By.XPATH, '//h2[@class="target-text" and text()="Selenium Webdriver"]')
        # self.assertTrue(target.text == expected_text, f'Target text {target.text} not matching expected text {expected_text}!')

    def test_3_display_button(self):
        self.click(self.BUTTON_DISPLAY_BUTTON)
        WebDriverWait(self.driver, 11).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button#hidden')))

    def test_4_button_enabled(self):
        self.click(self.BUTTON_ENABLE)
        WebDriverWait(self.driver, 11).until_not(EC.element_attribute_to_include((By.CSS_SELECTOR, 'button#disable'),'disabled'))

    def test_5_verify_checkbox(self):
        self.click(self.BUTTON_CHECKBOX)
        WebDriverWait(self.driver, 11).until(EC.element_located_to_be_selected((By.CSS_SELECTOR, 'input#ch')))











