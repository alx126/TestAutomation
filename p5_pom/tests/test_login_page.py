import unittest

from p5_pom.pages.login_page import LoginPage
from p5_pom.utils.driverfactory import DriverFactory


class TestLoginPage(unittest.TestCase):

    MAIN_ERROR_MESSAGE = "Login was unsuccessful. Please correct the errors and try again.\nNo customer account found"
    EMPTY_EMAIL_ERROR_MESSAGE = "Please enter your email"
    WRONG_EMAIL = "email.exemplu@yahoo.com"
    WRONG_PASS = "somepass"

    def setUp(self):
        self.driver = DriverFactory.get_driver()

    def tearDown(self):
        self.driver.quit()

    def test_login_with_unregistered_email(self):
        login_page = LoginPage(self.driver)

        login_page.navigate_to_login_page()
        login_page.set_email(self.WRONG_EMAIL)
        login_page.set_password(self.WRONG_PASS)
        login_page.click_login_button()

        self.assertTrue(login_page.is_main_error_message_displayed(), "Main error message not displayed.")
        self.assertEqual(login_page.get_main_error_message_text(), self.MAIN_ERROR_MESSAGE, "Unexpected error message.")

    def test_login_with_empty_email_and_pass(self):
        login_page = LoginPage(self.driver)

        login_page.navigate_to_login_page()
        login_page.click_login_button()

        self.assertTrue(login_page.is_email_error_message_displayed(), "Email error message not displayed.")
        self.assertEqual(login_page.get_email_error_message_text(), self.EMPTY_EMAIL_ERROR_MESSAGE, "Unexpected error "
                                                                                                    "message.")