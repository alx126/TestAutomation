import unittest
from pom.pages.forgot_password_page import ForgotPasswordPage
from pom.pages.login_page import LoginPage
from pom.utils.driverfactory import DriverFactory


class TestForgotPasswordPage(unittest.TestCase):
    INVALID_EMAIL = "asdf"
    INVALID_EMAIL_ERROR_MESSAGE = "Wrong email"
    ENTER_EMAIL_ERROR_MESSAGE = "Enter your email"

    def setUp(self):
        self.driver = DriverFactory.get_driver()

    def tearDown(self):
        self.driver.quit()

    def test_recover_password_with_invalid_email(self):
        login_page = LoginPage(self.driver)
        forgot_password_page = ForgotPasswordPage(self.driver)

        login_page.navigate_to_login_page()
        login_page.click_forgot_password_link()
        forgot_password_page.set_email(self.INVALID_EMAIL)
        forgot_password_page.click_recover_button()
        self.assertTrue(forgot_password_page.is_email_error_message_displayed(), "Error message not displayed")
        self.assertEqual(forgot_password_page.get_email_error_message_text(), self.INVALID_EMAIL_ERROR_MESSAGE,
                         "Error message not displayed")

    def test_recover_password_with_empty_email(self):
        login_page = LoginPage(self.driver)
        forgot_password_page = ForgotPasswordPage(self.driver)

        login_page.navigate_to_login_page()
        login_page.click_forgot_password_link()

        forgot_password_page.click_recover_button()
        self.assertTrue(forgot_password_page.is_email_error_message_displayed(), "Error message not displayed")
        self.assertEqual(forgot_password_page.get_email_error_message_text(), self.ENTER_EMAIL_ERROR_MESSAGE,
                         "Error message not displayed")