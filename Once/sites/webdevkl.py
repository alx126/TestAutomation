from selenium import webdriver
from Once.sites.base_site import BaseSite


class WebDevKL(BaseSite):

    def __init__(self, driver: webdriver):
        super().__init__(driver)

    WEBDEVKL_URL = "https://o360webdevkl.azurewebsites.net/"

    def navigate_to_login_page(self):
        self.driver.get(self.WEBDEVKL_URL)