from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Once.sites.base_site import BaseSite


class WebDev(BaseSite):

    def __init__(self, driver: webdriver):
        super().__init__(driver)

    WEBDEV_URL = "https://o360webdev.azurewebsites.net/"

    def navigate_to_login_page(self):
        self.driver.get(self.WEBDEV_URL)