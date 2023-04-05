import argparse
import sys
import unittest

import HtmlTestRunner

from pom.tests.test_forgot_password_page import TestForgotPasswordPage
from pom.tests.test_login_page import TestLoginPage


class TestSuite(unittest.TestCase):

    def test_suite(self):  # numele metodei este predefinit si NU trebuie schimbat

        teste_de_rulat = unittest.TestSuite()

        # adaugam testele in suita
        teste_de_rulat.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestForgotPasswordPage),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestLoginPage),
        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title="Test report",
            report_name="Test Results"
        )

        runner.run(teste_de_rulat)

