from selenium import webdriver

from p5_pom.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ForgotPasswordPage(BasePage):

    EMAIL_INPUT = (By.ID, "Email")
    RECOVER_BUTTON = (By.CLASS_NAME, "password-recovery-button")  # sau XPATH //button[text()='Recover']
    ERROR_MESSAGE_EMAIL = (By.ID, "Email-error")

    FORGOT_PASSWORD_PAGE_URL = "https://demo.nopcommerce.com/passwordrecovery"

    def __init__(self, driver: webdriver):
        super().__init__(driver)

    def set_email(self, email):
        self.type(self.EMAIL_INPUT, email)

    def is_email_error_message_displayed(self):
        return self.is_element_displayed(self.ERROR_MESSAGE_EMAIL)

    def get_email_error_message_text(self):
        return self.get_element_text(self.ERROR_MESSAGE_EMAIL)

    def click_recover_button(self):
        self.click(self.RECOVER_BUTTON)