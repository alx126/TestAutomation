import unittest

import HtmlTestRunner

from p3_selenium_intro.Tema_s9 import Login

from test_01_alerts import TestAlerts
from test_02_authentication import TestFirefoxAuthentication
from test_03_context_menu import TestContextMenu
from test_04_keys import TestKeys
from test_05_dropdown import TestDropdown


class Suita_tema10(unittest.TestCase):

    def test_suite(self):  # numele metodei este predefinit si NU trebuie schimbat

        # declaram o variabila TestSuite numit teste_de_rulat
        # prin intermediul acestui obiect vom accesa metoda addTests din clasa TestSuite
        # metoda addTests primeste ca si parametru o lista de teste care se doreste a fi executate
        # testele vor fi separate prin virgula
        # teste_de_rulat.addTest([]) -> apelare fara parametru
        suita_tema_10 = unittest.TestSuite()

        suita_tema_10.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Login),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestAlerts),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestFirefoxAuthentication),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestContextMenu),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestKeys),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestDropdown)
        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,  # vrem sa ne genereze un singur raport pentru toate clasele
            report_title="Raport teste Tema 10",
            report_name="Test Results"
        )

        runner.run(suita_tema_10)