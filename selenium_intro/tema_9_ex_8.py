from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Login(TestCase):
    driver = None
    LINK = "https://the-internet.herokuapp.com/"
    BUTTON_LOGIN = (By.XPATH, "//i[text()=' Login']")
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    ERROR_MESSAGE = (By.ID, "flash")
    ERROR_CLOSE = (By.CLASS_NAME, "close")
    SUCCES = (By.CLASS_NAME, "flash.success")

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.LINK)
        self.driver.maximize_window()
        self.driver.find_element(By.LINK_TEXT, "Form Authentication").click()
        self.driver.implicitly_wait(1)

    def tearDown(self):
        self.driver.quit()

    # metoda care primeste ca paramentru un locator
    # returneaza true daca elementul este prezent in pagina
    # sau false daca nu este prezent
    def is_element_present(self, element_locator):
        return len(self.driver.find_elements(*element_locator)) > 0

    def wait_for_element_to_be_absent(self, element_locator, seconds_to_wait):
        wait = WebDriverWait(self.driver, seconds_to_wait)
        return wait.until(EC.none_of(EC.presence_of_element_located(element_locator)))

    """
    Lasă goale user și pass
    Click login
    Apasă x la eroare
    Verifică dacă eroarea a dispărut
    """
    def test_empty_login_x(self):
        self.driver.find_element(*self.BUTTON_LOGIN).click()
        error = self.driver.find_element(*self.ERROR_MESSAGE)
        self.assertTrue(error.is_displayed(), "Error message is not displayed")

        self.driver.find_element(*self.ERROR_CLOSE).click()
        self.wait_for_element_to_be_absent(self.ERROR_MESSAGE, 2)

        assert not self.is_element_present(self.ERROR_MESSAGE)