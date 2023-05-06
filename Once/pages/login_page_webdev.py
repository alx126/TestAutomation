import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from Once.sites.webdev import WebDev


class LoginPageWebDev(WebDev):

    def __init__(self, driver: webdriver):
        super().__init__(driver)

    EMAIL_INPUT_ADMIN = (By.CSS_SELECTOR, 'input#logonIdentifier')
    PASSWORD_INPUT_ADMIN = (By.CSS_SELECTOR, 'input#password')
    EMAIL_INPUT_ENGSYS = (By.CSS_SELECTOR, 'input#i0116')
    PASSWORD_INPUT_ENGSYS = (By.CSS_SELECTOR, 'input#i0118')
    BUTTON_SIGN_IN = (By.CSS_SELECTOR, 'button#next')
    BUTTON_ENGSYS = (By.CSS_SELECTOR, 'button#EngSys')
    BUTTON_NEXT = (By.CSS_SELECTOR, 'input#idSIButton9')
    CHK_BOX_DONT_SHOW_AGAIN = (By.CSS_SELECTOR, 'input#KmsiCheckboxField')

    USER_ADMIN = 'admin@engsys360dev.onmicrosoft.com'
    PASSWORD_ADMIN = 'Es2K-Es2K'
    USER_ENGSYS = 'alex.parepa@once.no'
    PASSWORD_ENGSYS = 'Edimay2614'


    def navigate_to_login_page(self):
        self.driver.get(self.WEBDEV_URL)

    def sign_in_admin(self):
        self.find(self.EMAIL_INPUT_ADMIN).send_keys(self.USER_ADMIN)
        time.sleep(1)
        self.find(self.PASSWORD_INPUT_ADMIN).send_keys(self.PASSWORD_ADMIN)
        time.sleep(1)
        self.click(self.BUTTON_SIGN_IN)
        time.sleep(1)
        self.driver.implicitly_wait(2)

    def sign_in_engsys(self):
        self.click(self.BUTTON_ENGSYS)
        self.driver.implicitly_wait(5)
        time.sleep(1)
        self.select_and_overwrite(self.EMAIL_INPUT_ENGSYS, self.USER_ENGSYS)
        time.sleep(1)
        self.click(self.BUTTON_NEXT)
        self.driver.implicitly_wait(5)
        time.sleep(1)
        self.write(self.PASSWORD_INPUT_ENGSYS, self.PASSWORD_ENGSYS)
        time.sleep(1)
        self.click(self.BUTTON_NEXT)
        self.driver.implicitly_wait(5)
        time.sleep(1)

        # aprobare manuala authenticator

        self.click(self.CHK_BOX_DONT_SHOW_AGAIN)
        self.click(self.BUTTON_NEXT)
        self.driver.implicitly_wait(3)
