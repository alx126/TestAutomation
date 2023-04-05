import unittest

import HtmlTestRunner

from teste.test_01_alerts import TestAlerts
from teste.test_02_authentication import TestFirefoxAuthentication
from teste.test_03_context_menu import TestContextMenu
from teste.test_04_keys import TestKeys
from teste.test_05_dropdown import TestDropdown

"""
########### Test suite
Un test suite (suita de teste) este o colectie care cuprinde mai multe teste
Vom instala libraria html-testrunner pentru a genera rapoarte

pip install html-testRunner 

Apoi vom putea rula suita si din terminal in urmatoarele moduri: 
    1) secvential, cu comanda: pytest _selenium_extras/test_suite.py
    
    2) mai multe in paralel, cu comanda: pytest _selenium_extras/test_suite.py -n 2
    unde -n 2 reprezinta numarul de teste care pot rula in paralel
"""


# pentru ca am importat toata libraria unittest (randul 1 din cod),
# trebuie sa o specificam in fata clasei TestCase modulul
class TestSuite(unittest.TestCase):

    def test_suite(self):  # numele metodei este predefinit si NU trebuie schimbat

        # declaram o variabila TestSuite numit teste_de_rulat
        # prin intermediul acestui obiect vom accesa metoda addTests din clasa TestSuite
        # metoda addTests primeste ca si parametru o lista de teste care se doreste a fi executate
        # testele vor fi separate prin virgula
        # teste_de_rulat.addTest([]) -> apelare fara parametru
        teste_de_rulat = unittest.TestSuite()

        # adaugam testele in suita
        teste_de_rulat.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestAlerts),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestFirefoxAuthentication),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestContextMenu),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestKeys),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestDropdown)
        ])

        # vom crea o variabila de tip HTMLTestRunner care ne ajuta in executarea testelor din suita
        # si ne va genera un raport HTML cu rezultatele testelor
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,  # vrem sa ne genereze un singur raport pentru toate clasele
            report_title="My first test report",
            report_name="Test Results"
        )

        runner.run(teste_de_rulat)